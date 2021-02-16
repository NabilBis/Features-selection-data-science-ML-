#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:39:33 2021

@author: macos
"""
import numpy as np
#import pandas as pd

class ContinuousNull:
    
    def __init__(self, col, col_name=""):
        self.variable = col
        self.var_name = col_name
        
    
    def aloha():
        print("Continuous Null")
        
        
    def drop_null_values(self):
        return self.variable.dropna()    

    
    def replace_null_data(self, method="mean"):
        dic = { "mean" : self.variable.replace(np.NaN, self.variable.mean()),
                "median" : self.variable.replace(np.NaN, self.variable.median()),
                "mode" : self.variable.replace(np.NaN, self.variable.mode())
              }
        return dic[method]
    
    def replace_with_value(self, val):
        return self.variable.replace(np.NaN, val)
    
    
    