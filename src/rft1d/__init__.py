
__version__ = '0.2.9'  # 2026-11-01

__all__ = ['distributions', 'geom', 'prob', 'random', 'get_config']

from . import distributions
from . import geom
from . import prob
from . import random
from . _support import get_config

randn1d      = random.randn1d
multirandn1d = random.multirandn1d

chi2         = distributions.chi2
f            = distributions.f
norm         = distributions.norm
t            = distributions.t
T2           = distributions.T2
