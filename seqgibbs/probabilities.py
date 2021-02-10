#
# ForwardModel Class
#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
import numpy as np


class OneDimSampler():
    r"""OneDimSampler Class:
    Class for the transition kernels of the dimensions of the states
    taken one at a time as in a Gibbs Sampler .

    In the Gibbs Sampler scenario, we update each dimension of the data
    at a time according to a probability distribution conditional only
    on the current values of the other dimension of the state at which we
    are at.

    This means that if at the current step we aim to update the jth dimension
    we do it according to the following formula:

    .. math::
        X_{j}^{(t)} \sim \pi_{X_{j}|X_{j}}(\cdot|
        X_{1}^{(t)}, \dots , X_{j-1}^{(t)}, X_{j+1}^{(t-1)},
        \dots X_{d}^{(t-1)})

    Parameters
    ----------
    sampler_func_name
        (function) Probability Distribution used to sample new
        value of state at the dimension we require.

    """

    def __init__(self, sampler_func_name):
        self.sampler_pdf = sampler_func_name

    def sample(self, current_state, loc_update):
        """
        Set the righthand side (dx/dt) function
        :param functionName: the function to plug in

        Parameters
        ----------
        current_state
            (array) Value of the current state the chain
            produced by the Gibbs Sampler is at.
        loc_update
            (int) Position of the dimension to update of the state the chain
            produced by the Gibbs Sampler.

        """
        if np.asarray(current_state).ndim != 1:
            raise ValueError(
                'Current state values storage format must be 1-dimensional')
        if len(current_state) <= loc_update:
            raise ValueError('Sum of serial interval values must be > 0.')
        if not isinstance(loc_update, int):
            raise TypeError('Value of location of update must be integer.')

        # Retain only the part of the state that parametrizes the sampler
        # i.e. X(-j)
        conditional_part_of_state = current_state[-(loc_update-1)]

        # Return a draw from the sampler's probability distribution
        return self.sampler_pdf(*conditional_part_of_state)
