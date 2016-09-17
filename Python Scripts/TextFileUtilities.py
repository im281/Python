# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:13:16 2012

@author: Iman
"""
import ChemSpiderQuery
import sys

class TextUtilities(object):

    #l = []
    def DispayFileContents(self,file):
        inFile = open(file,'r')
        for line in inFile:
            print line.rstrip()
        inFile.close()
        
   
        
    def Write(self):
        print 'asdfsadfasf'
    
    def WriteTextFile(self,outfilename):
        outfile = open(outfilename, 'w')
        outfile.write('Line # 1\n')
        outfile.write('Line # 2\n')
        outfile.write('Line # 3\n')
        outfile.close()
        
                
    def ChemSpiderSearchFile(self,file):
        inFile = open(file,'r')      
        for line in inFile:
            c = ChemSpiderQuery.find(line)
            
            print 
            if c is None:
                 print 'none'
            else:
                for item in c:
                    #l.append(item)
                    sys.stdout.write(item.commonname + "@")
                    a = str(item.monoisotopicmass)
                    sys.stdout.write(a)
                    #print item.commonname print item.monoisotopicmass
                   
                
            
       
           
        inFile.close()  
       
        
    
#


       
            
            
            
            
            
            
            
