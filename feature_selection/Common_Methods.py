#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:44:29 2021

@author: macos
"""

from sklearn.preprocessing import StandardScaler 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import shapiro


class CommonMethods:
    
    def __init__(self, data):
        self.data = data
        
        
    def important_features(self, cols_names):
        stdsc = StandardScaler() 
        X_std = stdsc.fit_transform(self.data[cols_names].iloc[:,range(0,len(cols_names))].values)
        cov_mat =np.cov(X_std.T)
        plt.figure(figsize=(10,10))
        sns.set(font_scale=1.5)
        hm = sns.heatmap(cov_mat,
                         cbar=True,
                         annot=True,
                         square=True,
                         fmt='.2f',
                         annot_kws={'size': 12},
                         cmap='coolwarm',                 
                         yticklabels=cols_names,
                         xticklabels=cols_names)
        plt.title('Covariance matrix showing correlation coefficients', size = 18)
        plt.tight_layout()
        plt.show()
        
    
    def correlation_heatmap(self):
        sns.heatmap(self.data.corr())
        
    def shapiro_wilks(self, var):#test if a variable is normaly dstributed
        is_normally_disributed = False
        stat, p = shapiro(var)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
            is_normally_disributed = True
#             print('Sample looks Gaussian (fail to reject H0)')
            print("Variable is normally distributed")
        else:
#             print('Sample does not look Gaussian (reject H0)')
            print("Variable is not normally distributed")
        return is_normally_disributed
    
    def var_histogram(self, bins=50):
        plt.hist(x=self.data, bins=bins, color='red', alpha=0.7, rwidth=0.85)