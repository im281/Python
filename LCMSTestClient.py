# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:06:29 2016

@author: Iman Mohtashemi
"""

#Example using the pyzml package for LCMS data
import pymzml
import Scan 
from LCMS import *
"""matrix algebra"""
from numpy  import *

#read the mzML file
msrun = pymzml.run.Reader("Tryp_Myo_1.mzML")

#get all the ms2 scans
scans = Getms2scans(msrun)

thescan = scans[234]

#example spectrum
spectrum = thescan

#print out all the mz intensity pairs
for mz, i in thescan.peaks:
    print(mz, i)
    
#function to get the mz intensity pairs
GetmziArray(thescan)

#my scan object example
s = Scan(2,2,1,1,thescan.peaks)

#another example but using the pymzml codes
s = Scan(2,spectrum.get('id'),
                        spectrum.get('MS:1000744'),
                        spectrum.get('MS:1000041'),
                        spectrum.centroidedPeaks)
                        
#print out the mz intensity arrays again
for mz, i in s.miArray:
    print(mz, i)

#normalize the intensities
ns = Normalizescanintensities(s,2000)

#plot
import numpy as np
import matplotlib.pyplot as plt

plt.plot(ns)


spec = pymzml.spec.Spectrum


x = XIC("Tryp_Myo_1.mzML",680.9178)
