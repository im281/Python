# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:06:18 2015

@author: iman.mohtashemi
"""

import numpy as np
from pylab import *
from KarpusStrong import ks_loop

x = np.random.randn(100)
y =  ks_loop(x, 0.9, 10)

stem(np.arange(x.size),x,)
xlabel('Samples')
ylabel('x')
show()

#stem(np.arange(y.size),y)
#xlabel('Samples')
#ylabel('y')
#show()
