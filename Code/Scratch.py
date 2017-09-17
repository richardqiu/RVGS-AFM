# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:07:20 2017

@author: Richard
"""

fileName = "AFM-Scan.wsf"

with open(fileName, "r") as scanFile:
    for line in scanFile:
        if line.find("Pixels in X:") != -1:
            print line
            xPixels = int(line[12:])
        if line.find("Lines in Y:") != -1:
            print line
            yPixels = int(line[11:])
            
print xPixels, yPixels


