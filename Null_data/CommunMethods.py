#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:00:03 2021

@author: macos
"""
import seaborn as sns
import pandas as pd 

class CommunMethods:
    
    
    def __init__(self, col, col_name=""):
        self.variable = col
        self.var_name = col_name
        
    
    def nulls_per_column(self):
        print(self.variable.isnull().sum())
        
    def visualize_null_value(self):
        frame = pd.DataFrame(self.variable)
        frame['ignore'] = 0
        sns.heatmap(frame.isnull(), yticklabels=False, cbar=False, cmap='viridis')  
        
    def rows_mask_with_nulls(self, data, rows=3):
        nulls_in_row = data.isnull().sum(axis=1)
        null_masks = nulls_in_row < rows
        print("There are {} rows with {} or more missing values".format(len(data)-len(data[null_masks]),rows))
        return null_masks 