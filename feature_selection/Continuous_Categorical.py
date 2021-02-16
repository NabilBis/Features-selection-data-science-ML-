#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:36:10 2021

@author: macos
"""
from Commun_Methods import Commun_Methods
from scipy.stats import pointbiserialr
from scipy.stats import spearmanr
from scipy.stats import kendalltau

class Continuous_Categorical:
    
    def __init__(self, continuous, categorical, continuous_name="", categorical_name =""):
        self.continuous_var = continuous
        self.categorical_var = categorical
        self.continuous_var_name = continuous_name
        self.categorical_var_name = categorical_name
    
    def hola():
        print(__name__)
    
    def __point_biserial_assumptions(self):
        continuous_var_normally_distributed = Commun_Methods.shapiro_wilks(self.continuous_var)
        categorical_var_dichotomous = False 
        if (len(self.categorical_var.unique()) == 2):
            categorical_var_dichotomous = True
        return continuous_var_normally_distributed and categorical_var_dichotomous
    
    
    def point_biserial_correlation(self, alpha=0.05):
         if self.__point_biserial_assumptions():
             coef, p = pointbiserialr(self.continuous_var, self.categorical_var)
             if p>alpha:
                 print("{} and {} are NOT correlated".format(self.continuous_var_name, self.categorical_var_name))
             else:
                 print("{} and {} are  correlated".format(self.continuous_var_name, self.categorical_var_name))
         else:
             print("Point biserial correlation measure the concordance of a NORMALLY distributed continuous variable and DICHOTOMOUS variable")

    

    def spearsman_rank(self, alpha=0.05):
        coef, p = spearmanr(self.continuous_var, self.categorical_var)
        print('Spearmans correlation coefficient: %.3f' % coef)
        are_correlated = False
        if p<=alpha:
            print("{} and {} are correlated".format(self.continuous_var_name, self.categorical_var_name))
            are_correlated = True
        else:
            print("{} and {} are NOT correlated".format(self.continuous_var_name, self.categorical_var_name))
        return are_correlated
            
      
    def keandall_rank(self, alpha=0.05):
        coef, p = kendalltau(self.continuous_var, self.categorical_var)
        print('Kendall correlation coefficient: %.3f' % coef)
        are_correlated = False
        if p<=alpha:
            print("{} and {} are NOT correlated".format(self.continuous_var_name, self.categorical_var_name))
            are_correlated = True
        else:
            print("{} and {} are correlated".format(self.continuous_var_name, self.categorical_var_name))
        return are_correlated
    
    def one_way_anova(self):
        pass
    
    
    def t_test(self):
        pass
   
methods_definitions = {
                        'point_biserial_correlation':{
                                "initial_conditions":["Categotical data must be dichotomous", "continuous variable should be approximately normally distributed and have equal variances for each category of the dichotomous variable (Levene's test of equality of variances)"],
                                "return type":"p_value",
                                "use":"correlation between a continuous and categorical variable",
                                "interpretation":"p<=alpha -> not correlated",
                                "remarks":[]
                                },
                        'spearsman_rank':{
                                "initial_conditions":[],
                                "return type":"p_value",
                                "use":"correlation between a continuous and categorical variable",
                                "interpretation":"p<=alpha -> not correlated",
                                "remarks":[]
                                },
                        'keandall_rank':{
                                "initial_conditions":[],
                                "return type":"p_value",
                                "use":"correlation between a continuous and categorical variable",
                                "interpretation":"p<=alpha -> not correlated",
                                "remarks":[]
                                }
                        
                        }