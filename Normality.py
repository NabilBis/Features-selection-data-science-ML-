#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:06:15 2021

@author: macos
"""
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson
from scipy.stats import boxcox

class Normality:
    
    
    def __init__(self, var, var_name=""):
        self.variable = var
        self.var_name = var_name
        
        
    def visualize(self):
        plot = qqplot(self.var, line="45", fit=True)
        
    def shapiro_wilks(self):#test if a variable is normaly dstributed
        is_normally_disributed = False
        stat, p = shapiro(self.var)
        print('Statistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
            is_normally_disributed = True
#             print('Sample looks Gaussian (fail to reject H0)')
            print("{} is normally distributed".format(self.var_name))
        else:
#             print('Sample does not look Gaussian (reject H0)')
            print("{} is not normally distributed".format(self.var_name))
        return is_normally_disributed
    
    
    def agostino(self, alpha=0.5):
         is_normally_disributed = False
         stat, p = normaltest(self.variable)
         if p > alpha:
             print("{} is normally distributed".format(self.var_name))
             is_normally_disributed = True
             return is_normally_disributed
        else:
            print("{} is not normally distributed".format(self.var_name))
        return is_normally_disributed
        
    
    def anderson_draling(self):
        result = anderson(self.data)
        print('stat=%.3f' % (result.statistic))
        for i in range(len(result.critical_values)):
            sl, cv = result.significance_level[i], result.critical_values[i]
            if result.statistic < cv:
                print('Probably Gaussian at the %.1f%% level' % (sl))
            else:
		        print('Probably not Gaussian at the %.1f%% level' % (sl))
                
    def normalize(self):
        normalized_data, lambdaa = boxcox(self.variable)
        return normalized_data