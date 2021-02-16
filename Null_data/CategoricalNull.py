#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:06:51 2021

@author: macos
"""
import numpy as np

class CategoricalNull:
    
    
    def __init__(self, col, col_name=""):
        self.variable = col
        self.var_name = col_name   
    
    def drop_null_values(self):
        return self.variable.dropna()
    
    def replace_null_data(self):
        unique_vals = self.variable.unique()
        dic = { i : 0 for i in unique_vals }
        #print(dic)
        for x in unique_vals:
            dic[x]=dic[x]+1
        max_key = max(dic, key=dic.get)
        #print(max_key)
        return self.variable.replace(np.NaN, max_key)
    
    def replace_with_value(self, val):
        return self.variable.replace(np.NaN, val)
    
    def count_nulls(self):
        print(self.variable.isnull().sum())
        
    def aloha():
        print("Categorical Null")