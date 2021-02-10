#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#

import unittest

import scipy.stats
import numpy as np
import numpy.testing as npt

import seqgibbs as gibbs


class TestOneDimSamplerClass(unittest.TestCase):
    """
    Test the 'OneDimSampler' class.
    """
    def test__init__(self):
        gibbs.OneDimSampler(scipy.stats.norm.rvs, sum)

        with self.assertRaises(TypeError):
            gibbs.OneDimSampler(0, sum)

        with self.assertRaises(TypeError):
            gibbs.OneDimSampler(scipy.stats.norm.rvs, 0)

    def test_sample(self):
        sampler = gibbs.OneDimSampler(scipy.stats.norm.rvs, sum)
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
            sampler.sample(np.array([[0, 0], [0, 0]]), 3)

        with self.assertRaises(ValueError):
            sampler.sample(np.array([[0, 0], [0, 0]]), '1')
