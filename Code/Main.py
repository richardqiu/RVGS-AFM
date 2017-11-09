# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:06:54 2017

@author: Richard
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import Tkinter as tk
from tkFileDialog import askopenfilename

from ReadScanParams import ReadScanParams
from ReadScanData import ReadScanData
from CalcHeightParams import HeightParams


root = tk.Tk()
File = askopenfilename()
root.destroy()

print "Working File: " + File
params = ReadScanParams(File)
Data =  ReadScanData(File, params.xPixels, params.yPixels)

#
#Uncomment if you want plotting
#Warning: makes program REALLY slow
#
# =============================================================================
# plt.imshow(Data, cmap = 'gray')
# 
# X = np.arange(-12.8, 12.8, 0.1)
# Y = np.arange(-12.8, 12.8, 0.1)
# X, Y = np.meshgrid(X, Y)
# 
# fig = plt.figure()
# ax = fig.add_subplot(111, projection = '3d')
# ax.plot_surface(X, Y, Data)
# 
# =============================================================================


height = HeightParams(Data)
printHeight = vars(height)
print ""
print "".join("%s: %s \n" %item for item in printHeight.items())

FlatData = []
for x in np.nditer(Data):
    FlatData = np.append(FlatData, x)

plt.hist(FlatData)
