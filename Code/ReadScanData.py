# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 21:00:31 2017

@author: Richard
"""

import numpy as np

def ReadScanData(FileName, xPixels, yPixels):
    Data = np.empty([yPixels, xPixels])
    i = j = 0
    with open(FileName, "r") as ScanFile:
            for line in ScanFile:
                if i >= 6 and j < xPixels:
                    Data[j,:] =  line.split()
                    j += 1
                if line == "\n" and i < 6 :
                    i += 1
    
    return Data