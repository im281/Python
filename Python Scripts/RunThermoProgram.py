# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 13:03:28 2012

@author: Iman
"""

# Import system modules
import os,sys,subprocess


#os.startfile("C:/Users/Iman/Documents/Visual Studio 2010/Projects/PythonExe/PythonExe/bin/Debug/PythonExe.exe")
#os.startfile("C:/Program Files/Thermo/Pinpoint/Pinpoint.exe")
print 'Thermo Employees must imput a password to run the Thermo application\nwithout accepting the end user license agreement(EULA)'

print 'Enter password:'

password = raw_input()

if(password == 'Thermo1'):
    print 'Select application:'
    print ' 1 = Pinpoint'
    print ' 2 = MetQuest'
    print ' 3 = Proteome Discoverer'
    print ' 4 = Excel'
    print 'Enter Value:'
    
else:
    print 'Incorrect password'
    sys.exit()
    
x = raw_input()

x = int(x) #Select application index

if x == 1:
    os.startfile("C:/Program Files/Thermo/Pinpoint/Pinpoint.exe")
    os.startfile("C:/Users/Iman/Documents/Visual Studio 2010/Projects/PythonExe/PythonExe/bin/Debug/PythonExe.exe")
    #subprocess.Popen("C:/Users/Iman/Documents/Visual Studio 2010/Projects/PythonExe/PythonExe/bin/Debug/PythonExe.exe", shell=False, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
elif x == 2:
    print 'Run other application'
elif x == 3:
   #Discoverer will not run with os.startfile 
   #os.startfile("C:/Program Files/Thermo/Discoverer 1.3/System/Release/Thermo.Discoverer.exe")
    subprocess.Popen('C:/Program Files/Thermo/Discoverer 1.3/System/Release/Thermo.Discoverer.exe -startServer', shell=False, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
elif x == 4:
     #subprocess.Popen('C:/Program Files/Microsoft Office/Office12/excel.exe', shell=False, stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=None)
    os.startfile("C:/Program Files/Microsoft Office/Office12/excel.exe")    

    


    
