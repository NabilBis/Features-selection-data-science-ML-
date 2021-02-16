#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:37:27 2021

@author: macos
"""
from ContinuousNull import ContinuousNull
from CategoricalNull import CategoricalNull
from CommunMethods import CommunMethods

import pandas as pd

if __name__ == "__main__":
    

    new_data = pd.DataFrame()
    data = pd.read_csv('/Users/macos/Desktop/train_ctrUa4K.csv')
    
    #print(len(data.columns))
    
    communMethods = CommunMethods(data)
    communMethods.nulls_per_column()
    
    categorical = CategoricalNull(data.Credit_History)
    '''
    #r = categorical.replace_null_data()
    r = categorical.replace_null_data()
    print(r)
    '''
    data.Credit_History = data.Credit_History.map({0:'zero', 1:'one'})
    cols = ["Gender", "Married", "Dependents", "Self_Employed", "Credit_History"]
    
    data_colmns = data.columns
    for c in cols:
        categorical.variable = data[c]
        r = categorical.replace_null_data()
        new_data[c] = categorical.replace_null_data() 
    
    print("---------  - - - - - - - -  ---------") 
    
    continuous = ContinuousNull(data.LoanAmount)
    
    outliers_masks = pd.read_csv('/Users/macos/Desktop/home/πthon/classification_problems/Outliers/Outliers_mask.csv')

    cols = ["LoanAmount", "Loan_Amount_Term"]
    
    # Normally should replace with the mean of the column without outliers
    for c in cols:
        mask = outliers_masks[c+'_mask']
        colonne = data[c]
        colonne = colonne[mask]
        continuous.variable = data[c]
        new_data[c] = continuous.replace_with_value(colonne.mean())
        
        
    #print(new_data.isnull().sum())   
    
    new_data_columns = new_data.columns
    
    missing_new_columns = set(data_colmns) - set(new_data_columns)

    for i in missing_new_columns:
        new_data[i] = data[i] 
        
    new_data.to_csv("Null_removed.csv", index=False)
    
    
    '''
    In summation, handling the missing data is crucial for a data science project. 
    However,the data distribution should not be changed while handling missing data. 
    Any missing data treatment method should satisfy the following rules:

    1. Estimation without bias — Any missing data treatment method should not change 
    the data distribution.
    2. The relationship among the attributes should be retained.
'''