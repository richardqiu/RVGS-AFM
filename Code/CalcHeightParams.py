# -*- coding: utf-8 -*-
"""
Created on Sat Nov 04 15:22:35 2017

@author: Richard
"""

import numpy as np

class HeightParams:
    
    def __init__(self, Data):
        
        size = float(np.size(Data, 0)*np.size(Data, 1))
        Sq = Ssk = Sku = Sz = Sa = mean = 0
        Sp = Sv = Data[0][0]
        
        for i in xrange(np.size(Data, 0)):
            for j in xrange(np.size(Data, 1)):
                mean += Data[i][j]
        mean /= size
        
        
        for i in xrange(np.size(Data, 0)):
            for j in xrange(np.size(Data, 1)):
                Sq += (Data[i][j])**2
                Ssk += (Data[i][j])**3
                Sku += (Data[i][j])**4
                Sa += np.abs(Data[i][j])
                
                if Data[i][j] > Sp:
                    Sp = Data[i][j] 
                if Data[i][j] - mean < Sv:
                    Sv = Data[i][j] 
                    
        Sq = np.sqrt(Sq/size)
        Ssk = (Ssk)/(size*(Sq**3))
        Sku = (Sku)/(size*(Sq**4))
        SaSum = Sa
        Sa = Sa/size
        Sz = Sp - Sv
    
        self.mean = mean
        self.RMS = Sq
        self.Skewness = Ssk
        self.Kurtosis = Sku
        self.MaxPeakHeight = Sp
        self.MaxValleyDepth = Sv
        self.ProfileHeight = Sz
        self.ArithmeticalMean = Sa
        
        
        