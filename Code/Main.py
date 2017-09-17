# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 23:06:54 2017

@author: Richard
"""

import Globals
import ReadScanParams

xPixels = 1
yPixels = 2

Globals.init()
ReadScanParams.ScanParams("AFM-Scan.wsf")

print Globals.xPixels, Globals.yPixels