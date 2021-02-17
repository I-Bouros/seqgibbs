#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE for copyright
# notice and full license details.
#

import unittest

import scipy.stats
import numpy as np
import numpy.testing as npt

import seqgibbs as gibbs


def fun(x):
    """
    Function returning the parameters of the normal sampler.
        mean = sum of elements of x
        variance = exp(|x|)/(1+exp(|x|))
    """
    return np.sum(x), np.exp(np.sum(x))/(np.exp(np.sum(x))+1)


class TestOneDimSamplerClass(unittest.TestCase):
    """
    Test the 'OneDimSampler' class.
    """
    def test__init__(self):
        onedsampler = gibbs.OneDimSampler(scipy.stats.norm.rvs, sum)

        self.assertEqual(onedsampler.cond_func, sum)
        self.assertEqual(onedsampler.sampler_pdf, scipy.stats.norm.rvs)

        with self.assertRaises(TypeError):
            gibbs.OneDimSampler(0, sum)

        with self.assertRaises(TypeError):
            gibbs.OneDimSampler(scipy.stats.norm.rvs, 0)

    def test_sample(self):
        sampler = gibbs.OneDimSampler(scipy.stats.norm.rvs, fun)
        current_state = np.array([1, 2, 0])
        loc_update = 3

        new_state = sampler.sample(current_state, loc_update)
        conditional_part_of_state = np.array([
            x for i, x in enumerate(
                new_state.tolist()) if i != (loc_update-1)])

        self.assertEqual(len(new_state), len(current_state))
        npt.assert_array_equal(conditional_part_of_state, np.array([1, 2]))

        with self.assertRaises(ValueError):
            sampler.sample(np.array([[0, 0], [0, 0]]), 1)

        with self.assertRaises(ValueError):
            sampler.sample(np.array([0, 0]), 3)

        with self.assertRaises(TypeError):
            sampler.sample(np.array([0, 0, 0]), 1.5)

        with self.assertRaises(ValueError):
            sampler.sample(np.array([0, 0, 0]), 0)
