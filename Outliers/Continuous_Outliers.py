#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:02:02 2021

@author: macos
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



class Continuous_Outliers:
    
    def __init__(self, variable, name):
        self.variable = variable
        self.var_name = name
        
    def tendecy_measures(self):
        print("        TENDECY MEASURES")
        print("Mean :")
        print(self.variable.mean())
        print("Median :")
        print(self.variable.median())
        print("Mode :")
        print(self.variable.mode())
        print("Min :")
        print(self.variable.min())
        print("Max :")
        print(self.variable.max())
        
    def measure_of_dispersion(self):
        print("        DISPERSION MEASURE")
        print("Range")
        print(self.variable.max()-self.variable.min())
        print("Quantiles : ")
        print(self.variable.quantile([.25, .5, .75]))
        print("Interquantile range :")
        iqr = self.variable.quantile(.75)-self.variable.quantile(.25)
        print(iqr)
        print("Variance :")
        print(self.variable.var())
        print("Standard Deviation :")
        print(self.variable.std())
        print("Lower inner fence :")
        qar = list(self.variable.quantile([.25, .5, .75]))
        print(qar[0]-1.5*iqr)
        print("Upper inner fence :")
        print(qar[2]+1.5*iqr)
        print("Lower outer fence :")
        print(qar[0]-3*iqr)
        print("Upper outer fence :")
        print(qar[2]+3*iqr)
        print("\n")
        
    
    def variable_visualization(self):

        def split_to_quartiles_arrays(arr):
            vals = list(arr.quantile([.25, .5, .75]))
            quartiles = []
            quartiles.append(arr[arr<vals[0]])
            mask = (arr>vals[0]) & (arr<vals[1])
            quartiles.append(arr[mask])
            mask = (arr>vals[1]) & (arr<vals[2])
            quartiles.append(arr[mask])
            quartiles.append(arr[arr>vals[2]])
            return quartiles
        
        plt.hist(x=self.variable, bins=50, color='red', alpha=0.7, rwidth=0.85)
        plt.title(self.var_name)
        
        
        quartiles = split_to_quartiles_arrays(self.variable)
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
        fig.suptitle(self.var_name + ' quartiles histograms')
        ax1.hist(x=quartiles[0], bins=50, color='magenta', alpha=0.7, rwidth=0.85)
        ax2.hist(x=quartiles[1], bins=50, color='orange', alpha=0.7, rwidth=0.85)
        ax3.hist(x=quartiles[2], bins=50, color='orange', alpha=0.7, rwidth=0.85)
        ax4.hist(x=quartiles[3], bins=50, color='brown', alpha=0.7, rwidth=0.85)
        
        
    def outliers_mask(self, add_weak=True):
        masks = []
        mean = self.variable.mean()
        standard_deviation = self.variable.std()
        in_mean_range_mask = (self.variable > mean-3*standard_deviation) & (self.variable < mean+3*standard_deviation)
        qar = list(self.variable.quantile([.25, .5, .75]))
        iqr = qar[2]-qar[0]
        weak_outliers_mask = (self.variable > qar[0]-1.5*iqr) & (self.variable < qar[2]+1.5*iqr)
        strong_outliers_mask = (self.variable > qar[0]-3*iqr) & (self.variable < qar[2]+3*iqr)


        if any(in_mean_range_mask):
            #print("Yeap mean range")
            masks.append(in_mean_range_mask)
         
        if any(strong_outliers_mask):
            #print("Yeap there are strong outliers")
            masks.append(strong_outliers_mask)
        
        if add_weak and any(weak_outliers_mask):
            masks.append(weak_outliers_mask)
        
        outliers_mask = pd.Series(np.full(len(self.variable), True))
        for mask in masks:
                outliers_mask &= mask

        return outliers_mask
    
    
    def conclusions(self):
        # Standard deviation : spread of the data from the mean
        # Normaly all of the data should be in the range [mean ±Standard deviation]
        # print the percentage of data that doesn't sit in this range
        print(self.var_name)
        mean = self.variable.mean()
        standard_deviation = self.variable.std()
        data_in_range = self.variable[(self.variable > mean-3*standard_deviation) & (self.variable < mean+3*standard_deviation)]
        print("{}% of data sit in the range(mean ± 3*standard_deviation) : [{}, {}]".format(len(data_in_range)/len(self.variable), mean-3*standard_deviation, mean+3*standard_deviation))
        qar = list(self.variable.quantile([.25, .5, .75]))
        iqr = qar[2]-qar[0]
        weak_outliers = self.variable[(self.variable > qar[0]-1.5*iqr) & (self.variable < qar[2]+1.5*iqr)]
        # FAUX !!!!!
        print("{}% of data are weak outliers".format(1 - len(weak_outliers)/len(self.variable)))
        strong_outliers = self.variable[(self.variable > qar[0]-3*iqr) & (self.variable < qar[2]+3*iqr)]
        print("{}% of data are strong outliers".format(1 - len(strong_outliers)/len(self.variable)))
        #print("-----")
        #print(len(strong_outliers))
        #print(strong_outliers.value_counts())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        