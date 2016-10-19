# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 16:38:11 2016

@author: Iman Mohtashemi
"""
#Examples using functions from a different file
from Functions import *
ForLoop(5)
WhileLoop(10)
IfElse(2323)

#Examples using a class 'TextUtilities'
import TextFileUtilities 
t = TextFileUtilities.TextUtilities()
t.WriteTextFile('pythontest.txt')
t.Write()
file = "MAPK.fasta"
t.DispayFileContents(file)

