# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:06:54 2017

@author: Richard
"""

#import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
from tkFileDialog import askopenfilename

from ReadScanParams import ReadScanParams
from ReadScanData import ReadScanData


root = tk.Tk()
File = askopenfilename( filetypes = ( ("Windows Script files", ".wsf"), ("All files", "*.*") ) )
root.destroy()

params = ReadScanParams(File)
Data =  ReadScanData(File, params.xPixels, params.yPixels)

plt.figure()
plt.imshow(Data, cmap = 'viridis')
plt.figure()
plt.imshow(Data, cmap = 'gray')

