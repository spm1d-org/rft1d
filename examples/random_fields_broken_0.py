
'''
Verbose broken (piecewise continuous) random field generation.

Note:
When FWHM gets large (2FWHM>nNodes), the data should be padded prior to filtering.
Use **rft1d.random.randn1d** for optional padding.
'''




import numpy as np
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt



#(0) Set parameters:
np.random.seed(12345)
nResponses = 8
nNodes     = 101
FWHM       = 20.0



#(1) Generate Gaussian 1D fields:
y          = np.random.randn(nResponses, nNodes)
#convolve with a Gaussian kernel:
sd         = FWHM / np.sqrt(8*np.log(2))
y          = gaussian_filter1d(y, sd, axis=1, mode='wrap')
#scale to unit variance:
'''
Restore filtered data to unit variance.

Smoothing independent unit-variance noise with a kernel g yields noise
with variance sum(g**2), so the scaling factor is 1 / sqrt( sum(g**2) ).

Acknowledgement: this correction was first seen in "randomtalk.m" by
Matthew Brett (Oct 1999), downloaded from
http://www.fil.ion.ucl.ac.uk/~wpenny/mbi/index.html on 1 Aug 2014.
The code below is implemented from the mathematics above.
'''
### define Gaussian kernel
t          = np.arange(  -0.5*(nNodes-1) , 0.5*(nNodes-1)+1  )
g          = np.exp(-(t**2) / (2*sd**2))
g         /= g.sum()
### scaling factor
scale      = 1.0 / np.sqrt( (g**2).sum() )
### scale the data:
y         *= scale


#(2)  Mask out particular regions:
nodes        = np.array([True]*nNodes) #nothing masked out
nodes[20:30] = False  #this region will be masked out
nodes[60:80] = False  #this region will be masked out
y[:,np.logical_not(nodes)] = np.nan


#(3) Plot:
plt.close('all')
plt.plot(y.T)
plt.plot([0,100], [0,0], 'k:')
plt.xlabel('Field position', size=16)
plt.ylabel('z', size=20)
plt.title('Broken (piecewise continuous) random fields', size=20)
plt.show()
