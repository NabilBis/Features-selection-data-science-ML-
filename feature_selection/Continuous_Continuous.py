#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:14:25 2021

@author: macos
"""

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from minepy import MINE #!pip install minepy
from scipy.spatial.distance import pdist, squareform

class Continuous_Continuous:
    
    def __init__(self, var1, var2, var1_name="", var2_name =""):
        self.var1 = var1
        self.var2 = var2
        self.var1_name = var1_name
        self.var2_name = var2_name
        
    def hola():
        print(__name__)
        
    def scatter_vars(self):
        plt.scatter(self.var1, self.var2)
        plt.xlabel(self.var1_name)
        plt.ylabel(self.var2_name)
        plt.show()
    
    
    def pearson_correlation(self):
        return self.var1.corr(self.var2, method ='pearson')   

    
    def heat_map(self, data):
        cor = data.corr()
        plt.figure(figsize=(10, 6))
        sns.heatmap(cor, annot=True)
        
    def maximal_information_coefficient(self):
        mine = MINE()
        mine.compute_score(self.var1, self.var2)
        m = mine.mic()
        return m
    
    
    def distance_correlation(self):
        X = np.atleast_1d(self.var1)
        Y = np.atleast_1d(self.var2)
        if np.prod(X.shape) == len(X):
            X = X[:, None]
        if np.prod(Y.shape) == len(Y):
            Y = Y[:, None]
        X = np.atleast_2d(X)
        Y = np.atleast_2d(Y)
        n = X.shape[0]
        if Y.shape[0] != X.shape[0]:
            raise ValueError('Number of samples must match')
        a = squareform(pdist(X))
        b = squareform(pdist(Y))
        A = a - a.mean(axis=0)[None, :] - a.mean(axis=1)[:, None] + a.mean()
        B = b - b.mean(axis=0)[None, :] - b.mean(axis=1)[:, None] + b.mean()
    
        dcov2_xy = (A * B).sum()/float(n * n)
        dcov2_xx = (A * A).sum()/float(n * n)
        dcov2_yy = (B * B).sum()/float(n * n)
        dcor = np.sqrt(dcov2_xy)/np.sqrt(np.sqrt(dcov2_xx) * np.sqrt(dcov2_yy))
        return dcor
    # 0: x and Y independent
    # 1 : 
    
methods_definitions = {'pearson_correlation':{
                                    "initial_conditions":"Normally distributed",
                                    "return type":"number between -1 and 1",
                                    "use":"determine the relationship between two continuous features",
                                    "interpretation":"± 0.50 and ± 1 -> strong correlation, ± 0.30 and ± 0.49->medium ",
                                    "remarks":["Test LINEAR relationship only", "Correlation is symmetric"]
                                               
                                    },
                        'maximal_information_coefficient': {
                                    "initial_conditions":None,
                                    "return type":"number between 0 and 1",
                                    "use":"dependence between two variables and whether they have a linear or other functional relationship",
                                    "interpretation":"A high MIC value (identic having 1) suggests a dependency, whereas MIC = 0 describes the relationship between two independent variables",
                                    "remarks":[]
                                   },
                        'distance_correlation':{
                                "initial_conditions":None,
                                "return type":"number between 0 and 1",
                                "use":"measures both linear and nonlinear association between two random variables",
                                "interpretation":"0 independent, 1 dependent",
                                "remarks":[]
                                }
                        }
 

