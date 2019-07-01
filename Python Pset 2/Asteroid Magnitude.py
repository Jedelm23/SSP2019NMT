import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import math

def mag(filename, xStar, yStar, wStar, mag, xRoid, yRoid, wRoid, xBlank, yBlank):
    #Part 
    starImg = fits.getdata(filename)
    rStar = int(wStar/2)
    star = starImg[(yStar-rStar):(yStar+rStar+1),(xStar-rStar):(xStar+rStar+1)]
    
    starSum = np.sum(star)
    
    #Part b
    sky = starImg[(yBlank-1):(yBlank+2),(xBlank-1):(xBlank+2)]
    avgSky = np.mean(sky)
    
    #Part c
    signal = starSum-(avgSky * len(star)**2)
    const = mag + 2.5*(math.log10(signal))

    #Part d
    rRoid = int(wRoid/2)
    roid = starImg[(yRoid-rRoid):(yRoid+rRoid+1),(xRoid-rRoid):(xRoid+rRoid+1)]
    roidSum = np.sum(roid)
    signal2 = roidSum - (avgSky*len(roid)**2)

    magRoid = -2.5*(math.log10(signal2))+const

    return magRoid


print(mag("sampleimage.fits", 173, 342, 5, 15.26, 351, 154, 3, 200, 200))
print(mag("sampleimage.fits", 355, 285, 5, 16.11, 351, 154, 3, 200, 200))
