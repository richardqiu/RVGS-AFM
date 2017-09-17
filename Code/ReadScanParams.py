# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:02:28 2017

@author: Richard
"""
import Globals

def ScanParams(fileName):
    with open(fileName, "r") as scanFile:
        for line in scanFile:
            if line.find("Pixels in X:") != -1:
                print line
                Globals.xPixels = int(line[12:])
            if line.find("Lines in Y:") != -1:
                print line
                Globals.yPixels = int(line[11:])
            

    
    