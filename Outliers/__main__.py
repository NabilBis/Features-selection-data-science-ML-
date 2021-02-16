#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:04:43 2021

@author: macos
"""
from Continuous_Outliers import Continuous_Outliers

import pandas as pd


if __name__ == "__main__":
    
    data = pd.read_csv('/Users/macos/Desktop/train_ctrUa4K.csv')
    
    # Extract Continuous Data
    continuous_features  = data[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']].copy()

    con = Continuous_Outliers(continuous_features.ApplicantIncome, "ApplicantIncome")
    
    dic = {}
        
    for var in continuous_features:
        con.variable = continuous_features[var]
        con.var_name = var
        outliers_mask = con.outliers_mask(add_weak=False)
        dic[var+'_mask']= outliers_mask      
    
    dic['Loan_ID'] = data['Loan_ID']
    outliers_mask_file = pd.DataFrame(dic)
    outliers_mask_file.to_csv("Outliers_mask.csv", index=False)
    print("Outliers mask exported")
















