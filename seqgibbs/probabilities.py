#
# ForwardModel Class
#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE.md for copyright
# notice and full license details.
#
# import numpy as np


class OneDimSampler():
    r"""OneDimSampler Class:
    Class for the models following a Branching Processes behaviour.

    In the branching process model, we track the number of cases
    registered each day, I_t, also known as the "incidence" at time t.

    The incidence at time t is modelled by a random variable distributed
    according to a Poisson distribution with a mean that depends on previous
    number of cases, according to the following formula:

    .. math::
        E(I_{t}^{\text(local)}|I_0, I_1, \dots I_{t-1}, w_{s}, R_{t}) =
            R_{t}\sum_{s=1}^{t}I_{t-s}w_{s}

    Always apply method :meth:`set_r_profile` before calling
    :meth:`BranchProModel.simulate` for a change of R_t profile!

    Parameters
    ----------
    initial_r
        (numeric) Value of the reproduction number at the beginning
        of the epidemic
    serial_interval
        (list) Unnormalised probability distribution of that the recipient
        first displays symptoms s days after the infector first displays
        symptoms.

    """

    def __init__(self, initial_r, serial_interval):
        pass
