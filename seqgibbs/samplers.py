#
# SysGibbsAlgo Class
#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
import numpy as np
import numpy.random

from seqgibbs import OneDimSampler


class SysGibbsAlgo():
    r"""SysGibbsAlgo Class:
    Class for the sampling algorithm known as the Gibbs Sampler which updates
    the dimensions of the states in a systematic way, i.e. 1st, 2nd, and so on.

    In any Gibbs Sampler scenario, we update each dimension of the data
    at a time according to a probability distribution conditional only
    on the current values of the other dimensions of the state at which we
    are at, which we wrap up in a :meth:`OneDimSampler` object.

    Parameters
    ----------
    num_dim
        (integer) Number of dimensions of the states the chain
        produced using the Gibbs Sampler is at.
    initial_state
        (array) Value of the initial state the chain
        produced by the Gibbs Sampler is at.

    Notes
    -----
    Always apply method add_1_d_sampler before calling
    run to load a sampler used for the update of each dimension!

    """

    def __init__(self, num_dim, initial_state=None):
        if not isinstance(num_dim, int):
            raise TypeError('Number of dimension of state must be integer.')
        if num_dim < 1:
            raise ValueError('Number of dimension of state must be positive.')

        # If no initial state is provided, assume zeros in all positions.
        if initial_state is None:
            initial_state = np.zeros(num_dim)

        # If provided, then check
        if np.asarray(initial_state).ndim != 1:
            raise ValueError(
                'Initial state storage format must be 1-dimensional')
        if len(initial_state) != num_dim:
            raise ValueError('Given initial state does not have stated \
                dimension size.')

        self.num_dim = num_dim
        self.initial_state = np.asarray(initial_state)
        self.current_state = np.copy(self.initial_state)
        self.one_d_samplers = []
        self.chain_states = [self.initial_state.tolist()]

    def change_initial_state(self, new_state):
        """
        Change initial state of the chain we sample using Gibbs algorithm.

        Parameters
        ----------
        new_state
            (array) Value of the new initial state of the chain
            produced by the Gibbs Sampler is at.

        """
        if np.asarray(new_state).ndim != 1:
            raise ValueError(
                'New state values storage format must be 1-dimensional')
        if len(new_state) != self.num_dim:
            raise ValueError(
                'New initial state does not have stated \
                dimension size.')

        self.initial_state = new_state

    def add_1_d_sampler(self, new_sampler):
        """
        Add unidimensional sampler to the list of the samplers
        used to update the dimensions of the states of the chain.

        Parameters
        ----------
        new_sampler
            (OneDimSampler) Unidimensional sampler used to draw new
            values for the updating dimension of the state.

        """
        if not isinstance(new_sampler, OneDimSampler):
            raise TypeError(
                'Sampler needs to be an instance of the \
                seqgibbs.OneDimSampler')

        self.one_d_samplers.append(new_sampler)

    def _one_cycle_routine(self):
        """
        Run one complete systematic scan update cycle of all the dimensions
        of the current state. Each dimension updates using one of
        unidimensional samplers found in the list. Return the new state.

        """
        # Updates dimensions 1, 2, ... d in order.
        # Uses the jth unidimensional sampler to update jth dimension.
        current_state = np.copy(self.current_state)

        for j in range(self.num_dim):
            current_state = self.one_d_samplers[j].sample(
                current_state, j+1)

        self.current_state = current_state

    def run(self, num_cycles, mode='restart'):
        """
        Add unidimensional sampler to the list of the samplers
        used to update the dimensions of the states of the chain.

        Parameters
        ----------
        num_cycles
            (integer) Number of complete cycles for which we run the
            Systematic Scan Gibbs. Corresponds to number of realizations
            in the final chain.
        mode
            (str) The regime in which we run the Gibbs Sampler.
            Two alternatives:
            - The ``restart`` mode restarts the chain from the initial
            specified state and runs it for ``num_cycles`` steps.
            - The ``continue`` mode runs the chain from the last known
            state and continues to run it for an additional ``num_cycles``
            steps.
        """
        # Read regime in which we run the Gibbs sampler
        if mode not in ['restart', 'continue']:
            raise ValueError(
                'No such regime for the sampling. Must be `restart` \
                or `continue`')
        if not isinstance(num_cycles, int):
            raise TypeError('Number of cycles must be integer.')
        if num_cycles < 1:
            raise TypeError('Number of cycles must be positive.')

        if mode == 'restart':
            # Restart chain from inital state
            self.chain_states = [self.initial_state.tolist()]
            self.current_state = np.copy(self.initial_state)

        # Run cycle routine num_cyles times
        for c in range(num_cycles):
            self._one_cycle_routine()
            self.chain_states.append(self.current_state.tolist())

        # Return full chain of states
        return self.chain_states


#
# RandGibbsAlgo Class
#

class RandGibbsAlgo(SysGibbsAlgo):
    r"""RandGibbsAlgo Class:
    Class for the sampling algorithm known as the Gibbs Sampler which updates
    the dimensions of the states in a random way, using a probability
    distribution.

    In any Gibbs Sampler scenario, we update each dimension of the data
    at a time according to a probability distribution conditional only
    on the current values of the other dimensions of the state at which we
    are at, which we wrap up in a :meth:`OneDimSampler` object.

    Parameters
    ----------
    num_dim
        (integer) Number of dimensions of the states the chain
        produced using the Gibbs Sampler is at.
    initial_state
        (array) Value of the initial state the chain
        produced by the Gibbs Sampler is at.
    dimen_prob
        (list) List of probabilities for choosing dimension to
        update in the sampling routine.

    Notes
    -----
    Always apply method add_1_d_sampler before calling
    run to load a sampler used for the update of each dimension!

    """
    def __init__(
            self, num_dim, initial_state=None, dimen_prob=None):

        # Import from SysGibbsAlgo class
        super().__init__(
            num_dim, initial_state, dimen_prob)

        # If no probabilities for choice of update provide, assume uniform.
        if dimen_prob is None:
            dimen_prob = np.ones(num_dim)

        # If provided, then check
        if np.asarray(dimen_prob).ndim != 1:
            raise ValueError(
                'Update probabilities storage format must be 1-dimensional')
        if len(dimen_prob) != num_dim:
            raise ValueError('Given update probability distribution do not \
                have stated dimension size.')

        self.dimen_prob = np.asarray(dimen_prob)

    def change_dimen_prob(self, new_probs):
        """
        Change probabilities for dimension update of the chain we sample using
        Gibbs algorithm.

        Parameters
        ----------
        new_probs
            (array) Value of the new probabilities for dimension update of the
            chain produced by the Gibbs Sampler is at.

        """
        if np.asarray(new_probs).ndim != 1:
            raise ValueError(
                'New update probability distribution storage format must be \
                    1-dimensional')
        if len(new_probs) != self.num_dim:
            raise ValueError(
                'New update probability distribution does not have stated \
                dimension size.')

        self.dimen_prob = new_probs

    def _one_cycle_routine(self):
        """
        Run one complete random scan update cycle of all the dimensions
        of the current state. Only dimension updated at a time using one of
        unidimensional samplers found in the list. The choice of simension to
        update is made at random, using a weighted sampling. Return the new
        state.

        """
        # Updates one of the dimensions 1, 2, ... d at random.
        # Uses the jth unidimensional sampler to update jth dimension.
        current_state = np.copy(self.current_state)

        j = np.random.choice(self.num_dim, 1, p=self.dimen_prob)
        current_state = self.one_d_samplers[j].sample(current_state, j+1)

        self.current_state = current_state
