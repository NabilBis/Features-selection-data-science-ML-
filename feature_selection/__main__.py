#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 18:37:19 2021

@author: macos
"""
from Categorical_Categorical import Categorical_Categorical

#import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#from scipy.stats import chi2_contingency
#from scipy.stats import chi2
#import seaborn as sns
#from scipy.stats import shapiro
#from scipy.stats import pointbiserialr


if __name__ == "__main__":
    
    data = pd.read_csv("/Users/macos/Desktop/home/πthon/classification_problems/Null_data/Null_removed.csv")
    
    target = data.Loan_Status
    
    #cat = ['Gender', 'Married', 'Dependents', 'Self_Employed', 'Property_Area', 'Credit_History', 'Education']
    
    categorical_cols = ['Gender', 'Married', 'Dependents', 'Self_Employed', 'Property_Area', 'Credit_History', 'Education']
    cat_cat = Categorical_Categorical(data.Dependents, target)
    
    print(cat_cat.cramers_v())
    print(cat_cat.chi_square())
    print(cat_cat.theil_u())
    ''' 
    dependent_cols = []
    
    
    for i in categorical_cols:
        cat_cat.var = data[i]
        if cat_cat.chi_square():
            dependent_cols.append(i)
        
        
    print(dependent_cols)
    '''
   
   
   
   # CONTINOUS AND CATEGORICAL FEATURE's SELECTION (Outliers included)
   
   
    '''
    conti_cat = Continuous_Categorical(data.ApplicantIncome, target)
    conti_cat.continuous_var_name = "ApplicantIncome"
    #continuous_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']


    
    for u in cat:
        conti_cat.categorical_var = data[u]
        conti_cat.categorical_var_name = u
        print(conti_cat.spearsman_rank())
   '''