# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:59:51 2015

@author: iman.mohtashemi
"""
class Scan:
    scanNumber = 0
    msOrder = 0
    precursorMass = 0
    chargeState = 0
    miArray = []
      # The class "constructor" - It's actually an initializer 
    def __init__(self,msorder,scan,precursor,charge,mi_array ):
        self.msOrder = msorder
        self.scanNumber = scan
        self.precursorMass = precursor
        self.chargeState = charge
        self.miArray = mi_array
        
        
        
        
        
        
class test:
    p1 = ""
    p2 = ""
    
    def add(self,x):        
        for i in range(x):
            k = i + i          
        return k
    
    
    
