'''
Datasets used by the example scripts.

This module is deliberately NOT part of the rft1d package -- rft1d itself
needs no data files.  Scripts in this directory can use it directly:

    >>> import _rft1d_data
    >>> weather = _rft1d_data.weather()

Scripts in ./paper/ need this directory on sys.path first:

    >>> import os, sys
    >>> sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    >>> import _rft1d_data

Current datasets include:

    * Weather (Ramsay & Silverman, 2005)
'''

# Copyright (C) 2026  Todd Pataky




def weather():
    '''
    Canadian weather dataset from the R package "fda" (version 6.1.9)
    by James Ramsay, Giles Hooker and Spencer Graves, distributed under
    the license "GPL (>= 2)":
    https://cran.r-project.org/package=fda
    (see the `./_datafiles/weather` directory).

    The dataset is described in:
    Ramsay JO, Silverman BW (2005). Functional Data Analysis
    (Second Edition), Springer, New York.
    Chapter 13: "Modelling functional responses with
    multivariate covariates"

    Data subsets include:

    - 'Atlantic'
    - 'Pacific'
    - 'Continental'
    - 'Arctic'


    :Example use:

    >>> weather = _rft1d_data.weather()
    >>> y = weather['Atlantic']  # (15 x 365) numpy array
    >>> from matplotlib import pyplot
    >>> pyplot.plot(y.T)
    '''
    import os
    import numpy as np
    fname    = os.path.join(os.path.dirname(__file__), '_datafiles', 'weather', 'CanadianWeather.npz')
    with np.load(fname) as Z:
        Y        = Z['dailyAv'][:,:,0].T
        region   = Z['region']
    D        = {name: Y[region==name]  for name in ('Atlantic', 'Pacific', 'Continental', 'Arctic')}
    return D
