#
# Root of the seqgibbs module.
# Provides access to all shared functionality (models, simulation, etc.).
#
# This file is part of SEQGIBBS
# (https://github.com/I-Bouros/seqgibbs.git) which is released
# under the MIT license. See accompanying LICENSE for copyright
# notice and full license details.
#
"""seqgibbs is a Sequential Gibbs Sampling Algorithm library.
It contains functionality for modelling, simulating, and visualising the
number of cases of infections by day during an outbreak of the influenza virus.
"""

# Import version info
from .version_info import VERSION_INT, VERSION  # noqa

# Import main classes
from .probabilities import OneDimSampler    # noqa
from .samplers import SysGibbsAlgo, RandGibbsAlgo    # noqa
