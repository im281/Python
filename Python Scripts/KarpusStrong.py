# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 16:05:31 2015

@author: iman.mohtashemi
"""

__author__ = 'iman.mohtashemi'

def ks_loop(x, alpha, D) :
    import numpy as np
    '''
    Length of the output signal must be larger than the length of the input signal,
    that is, D must be larger than 1
    '''
    if D < 1:
        print('Duration D must be greater than 1')

    # Make sure the input is a row-vector
    if x.ndim != 1:
        print('The array entered is of the wrong size')
        return None

    # Number of input samples
    M = len(x)

    # N umber of output samples
    size_y = D*M

    # Initialize with random input x
    y = np.zeros((size_y,1))
    for i in range(M):
        y[i] = x[i]

    for index in range(M,size_y):
        y[index] = float(alpha * y[index - M])

    return y

def ks(x, alpha, D) :
    import numpy as np
    #   Length of the output signal must be larger than the length of the input signal,
    #   that is, D must be larger than 1 
    if D < 1:
        print('Duration D must be greater than 1')
        
    #   Make sure the input is a row-vector
    if x.ndim != 1:
        print('The array entered is of the wrong size')
        return None
    #   Number of input samples
    M = len(x)
    
    #   Create a vector of the powers of alpha, [alpha^0 alpha^1 ....]
    a = np.ones((1,D)) * alpha
    b = np.arange(D)
    alphaVector = pow(a,b)
    
    #Create a matrix with M columns, each being the vector of the powers of alpha
    alphaMatrix = np.eye(D,M) 
    for index in range(M):
        alphaMatrix[:,index] = alphaVector
        
    #Create a matrix with D rows filled by the input signal x  
    xMatrix = np.tile(x,(D,1))
    
    #Multipliy the two, so we can read it out
    #column-by-column
    yMatrix = alphaMatrix * xMatrix
    
    #Read out the output column by columnn
    y = yMatrix.flatten()
        
    return y
    
    
    
def GeneralDecay(x, alpha, D) :
    import numpy as np
    '''
    Length of the output signal must be larger than the length of the input signal,
    that is, D must be larger than 1
    '''
    if D < 1:
        print('Duration D must be greater than 1')

    # Make sure the input is a row-vector
    if x.ndim != 1:
        print('The array entered is of the wrong size')
        return None

    # Number of input samples
    M = len(x)
    
    # Initialize with random input x
    y = np.zeros((M,1))
    for i in range(M):
        y[i] = x[i]

    for index in range(0,len(x)):
        y[index] = float(alpha * y[index - D]) + x[index]

    return y