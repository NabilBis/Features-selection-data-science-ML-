#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:32:29 2021

@author: macos
"""
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from scipy.stats import chi2
from collections import Counter
import scipy.stats as ss
import math
#import seaborn as sns
#from scipy.stats import shapiro
#from scipy.stats import pointbiserialr

class Categorical_Categorical:
    
    def __init__(self, var, target, var_name="", target_name =""):
        self.var = var
        self.target = target
        self.var_name = var_name
        self.target_name = target_name
      
    def crosstab(self):
        #Better compute cross_tab one_time
        cross_tab = pd.crosstab(self.var, self.target)
        print(cross_tab)
        cross_tab.plot(kind='bar', stacked=True, color=['red','blue'], grid=False)
        
        
    def chi_square(self, prob = 0.95):
        # Assumptions : - Your categorical variable should be dichotomous 
        # - Contingency coefficient C cannot be used to compare associations among tables 
        # with different numbers of categories or in tables with a mix of categorical and continuous variables
        are_dependent = False
        cross_tab = pd.crosstab(self.var, self.target)
        stat, p, dof, expected = chi2_contingency(cross_tab)
        # interpret test-statistic
        critical = chi2.ppf(prob, dof)
        alpha = 1.0 - prob
#         print('probability = %.3f, critical = %.3f, stat = %.3f' % (prob, critical, stat))
        if abs(stat) >= critical:
#             print('{} & {} are Dependent'.format(self.var1_name, self.var2_name))
            are_dependent = True
#         else:
#             print('{} & {} are Independent'.format(self.var1_name, self.var2_name))
        # interpret p-value
#         alpha = 1.0 - prob
#         print('significance=%.3f, p=%.3f' % (alpha, p))
        #if p <= alpha:
            #are_dependent = True
#             print('{} & {} are Dependent'.format(self.var1_name, self.var2_name))
#         else:
#             print('{} & {} are Independent'.format(self.var1_name, self.var2_name))
            
        return are_dependent
    
    def cramers_v(self):
        confusion_matrix = pd.crosstab(self.var, self.target)
        chi2 = chi2_contingency(confusion_matrix)[0]
        n = confusion_matrix.sum().sum()
        phi2 = chi2/n
        r,k = confusion_matrix.shape
        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)
        res = np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))
        #res ~ 0 no association, ~ 1 full association
        #pitfall : losing valuable information due to symmetry
        return res
    
    
    def conditional_entropy(self, x, y):
        # entropy of x given y
        y_counter = Counter(y)
        xy_counter = Counter(list(zip(x,y)))
        total_occurrences = sum(y_counter.values())
        entropy = 0
        for xy in xy_counter.keys():
            p_xy = xy_counter[xy] / total_occurrences
            p_y = y_counter[xy[1]] / total_occurrences
            entropy += p_xy * math.log(p_y/p_xy)
        return entropy

    def theil_u(self):
        s_xy = self.conditional_entropy(self.var, self.target)
        x_counter = Counter(self.var)
        total_occurrences = sum(x_counter.values())
        p_x = list(map(lambda n: n/total_occurrences, x_counter.values()))
        s_x = ss.entropy(p_x)
        if s_x == 0:
            return 1

        return (s_x - s_xy) / s_x
        
    
        
    def fisher_score(self):
        pass
    
    def goodman_krushals_lambda(self):
        pass
    
    def gini_index(self):
        pass
    
    

methods_definitions = {'chi_square':{
                                    "initial_conditions":None,
                                    "return type":"p_value/statistics",
                                    "use":"determine the relationship between two categorical features",
                                    "interpretation":"high Chi-Square value indicates that the hypothesis of independence is incorrect",
                                    "remarks":["sensitive to small frequencies in cells of tables"]
                                               
                                    },
                      "cramers_v":{
                                    "initial_conditions":None,
                                    "return type":"number between 0 and 1",
                                    "use":"he intercorrelation of two discrete variables",
                                    "interpretation":"0 (corresponding to no association between the variables) to 1 (complete association)",
                                    "remarks":["Note that as chi-squared values tend to increase with the number of cells, the greater the difference between r (rows) and c (columns), the more likely φc will tend to 1 without strong evidence of a meaningful correlation"]
                                    },
                      "conditional_entropy":{
                                    "initial_conditions":0,
                                    "return type":0,
                                    "use":0,
                                    "interpretation":0,
                                    "remarks":0
                                    },
                      "theil_u":{
                                    "initial_conditions":None,
                                    "return type":"number between 0 and 1,
                                    "use":"measure of association between two categorical features",
                                    "interpretation":"0 (corresponding to no association between the variables) to 1 (complete association)",
                                    "remarks":["also referred to as the Uncertainty Coefficient"]
                                    }
                      }
