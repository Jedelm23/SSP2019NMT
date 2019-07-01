

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import math


data = np.array([[0,33,21,33,8],
                 [0,56,51,53,26],
                 [23,120,149,73,18],
                 [55,101,116,50,16],
                 [11,78,26,2,10]]) 

def centroidSpecific (data):
    total = np.sum(data)
    x = []
    for column in range(len(data)):
        x.append(np.sum(data[:,column]))

    xSum = 0
    for i in range(len(x)):
        xSum += x[i]*i
        
    xBar = xSum/total
    
    y = []
    for row in range(len(data)):
        y.append(np.sum(data[row,:]))
    
    ySum = 0
    for i in range(len(y)):
        ySum += y[i]*i
    yBar = ySum/total   

    return xBar,yBar

print(centroidSpecific(data))

def Centroid(filename, xCoord, yCoord, radius):
    #Get File
    im = fits.getdata(filename)
    imSlice = im[(yCoord-radius):(yCoord+radius+1),(xCoord-radius):(xCoord+radius+1)]
    
    #Find Centroid
    total = np.sum(imSlice)
    x = []
    for column in range(len(imSlice)):
        x.append(np.sum(imSlice[:,column]))

    xSum = 0
    for i in range(len(x)):
        xSum += x[i]*i
    xBar = (xSum/total)+xCoord-radius
    
    y = []
    for row in range(len(imSlice)):
        y.append(np.sum(imSlice[row,:]))
    
    ySum = 0
    for i in range(len(y)):
        ySum += y[i]*i
    yBar = (ySum/total)+yCoord-radius

    #Finding Standard Deviation of the Mean
    xDev = []
    xDevSum = 0
    for i in range(len(imSlice)):
        xDev.append(-i+xBar-xCoord+radius)
    for i in range(len(xDev)):
        xDevSum += x[i]*(xDev[i])**2

    xStandard = (xDevSum/((total-1)*total))**.5

    yDev = []
    yDevSum = 0
    
    for i in range(len(imSlice)):
        yDev.append(-i+yBar-yCoord+radius)
    for i in range(len(yDev)):
        yDevSum += y[i]*(yDev[i])**2
        
    yStandard =(yDevSum/((total-1)*total))**.5
    
    return(xBar,yBar,xStandard,yStandard)

print(Centroid("sampleimage.fits", 351,154,3))

    
    
    
