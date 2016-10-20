# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:23:55 2015

@author: iman.mohtashemi
"""

import pymzml
from Scan import *
"""matrix algebra"""
from numpy  import *

#msrun = pymzml.run.Reader("C:/Users/iman.mohtashemi/Desktop/Test Files/Tryp_HCD.mzML")


def GetmziArray(spectrum):
    for mz, i in spectrum.peaks:
        print(mz, i)
               
def Getms2scans(x):
    ms2scans = []
    for spectrum in x:
        if(spectrum['ms level'] == 2):
            ms2scans.append(spectrum)
            print ('ms2')
        else:
            print ('ms1')
            
    return ms2scans

def Getms2scans1(x):
    ms2scans = []
    for spectrum in x:
            if spectrum['ms level'] == 2:
                s = Scan(2,spectrum.get('id'),
                         spectrum.get('MS:1000744'),
                         spectrum.get('MS:1000041'),
                         spectrum.centroidedPeaks)
                ms2scans.append(s)
    return ms2scans
                
def Getms2scanpeaks(x):
    ms2scans = []
    for spectrum in x:
          if(spectrum['ms level'] == 2):
              ms2scans.append(spectrum.centroidedPeaks)
    return ms2scans
    
    
def Normalizescanintensities(scan,bins):
    '''create empty array with length of mass/intensity array'''
    arr = zeros(shape = (bins,1))
    for i in range(len(scan.miArray)):
        arr[i] = scan.miArray[i][1]
    for j in range(len(arr)):
        arr[j] = (arr[j]/arr.max())*100
        
    return arr
    
    
    

def XIC(file,MASS_2_FOLLOW):
    run = pymzml.run.Reader(file, MS1_Precision = 20e-6, MSn_Precision = 20e-6)
    timeDependentIntensities = []
    for spectrum in run:
        if spectrum['ms level'] == 1:
            matchList = spectrum.hasPeak(MASS_2_FOLLOW)
            if matchList != []:
                for mz,I in matchList:
                    timeDependentIntensities.append( [ spectrum['scan time'], I , mz ])
                    for rt, i, mz in timeDependentIntensities:
                        print('{0:5.3f} {1:13.4f}       {2:10}'.format( rt, i, mz ))
                        
    return timeDependentIntensities 
    
    
    
#def PlotSpectrm(file):    
#mzMLFile = 'profile-mass-spectrum.mzml'
#example_file = get_example_file.open_example(mzMLFile)
#run = pymzml.run.Run("../mzML_example_files/"+mzMLFile, precisionMSn = 250e-6)
#p = pymzml.plot.Factory()
#for spec in run:
#     p.newPlot()
#     p.add(spec.peaks, color=(200,00,00), style='circles')
#     p.add(spec.centroidedPeaks, color=(00,00,00), style='sticks')
#     p.add(spec.reprofiledPeaks, color=(00,255,00), style='circles')
#     p.save( filename="output/plotAspect.xhtml" , mzRange = [745.2,745.6] 
    
    
        
#ms2scans = Getms2scans1(msrun)
#test = msrun[2547]
#n = Normalizescanintensities(test,2000)
#import matplotlib.pyplot as plt







