# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 12:44:36 2015

@author: iman.mohtashemi
"""

import numpy as np
from pylab import *
from KarpusStrong import GeneralDecay
import MSPlot


#import matplotlib.pyplot as plt
#from matplotlib.finance import candlestick
#import matplotlib
#import pylab
#matplotlib.rcParams.update({'font.size': 9})
#t = arange(-2, 11.0, 1)

#s = (cos(pi*.1*t) + cos(pi*.1*(t-1)))/2
##s = (cos(pi*t) + cos(pi*(t-1)))/2
##s = 1.05*s*(t-1) + t
##pl.bar(t, s, facecolor='#9999ff', edgecolor='red')
#stem(t,s)




x = np.random.randn(40)

for i in range(len(x)):
    x[i] = 0
x[3] = 1    
y =  GeneralDecay(x, .7, 3)
stem(y)


