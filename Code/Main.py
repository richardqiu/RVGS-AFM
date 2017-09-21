# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:06:54 2017

@author: Richard
"""

#import numpy as np
import matplotlib.pyplot as plt

from ReadScanParams import ReadScanParams
from ReadScanData import ReadScanData

File = "AFM-Scan.wsf"

params = ReadScanParams(File)
Data =  ReadScanData(File, params.xPixels, params.yPixels)

plt.figure()
plt.imshow(Data, cmap = 'viridis')
plt.figure()
plt.imshow(Data, cmap = 'gray')

