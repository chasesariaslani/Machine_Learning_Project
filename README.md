# Machine_Learning_Project
Machine Learning Project for NYCDSA

This project is based off of the Kaggle competition: Attempting to Predict the Housing Sale Price given features of the house.

In order to run this properly, You must follow these steps:
1. Have the train.csv in the directory with all the coding files.
2. Run Data_Cleaning.R
  - Creates EDA_Cleaned.csv
3. Run EDA_modification.py
  - Creates Nominal.csv
    -- Description: All nominal features of house
  - Creates Numeric.csv
    -- Description: All numerical features of house
  - Creates Ordinal.csv
    -- Description: All ordinal Features of house.
  - Creates EDA_final.csv
    -- Description: All features of house in one file.
  - Creates SalPrice_final.csv
    -- Description: Response variable.
4. Run Data_Analysis.ipynb
  - Shows some interesting feature analyses.
5. Run Feature_Importances.ipynb
  - Allows a walkthrough of features that are important as well as the regressions (from lasso to forest regressions)
6. Optional: AIC and Multiple Linear Regression Assumptions.R
  - Shows Coefficient of Determination (R^2) when following the AIC.
  - Shows Assumptions of Multiple Linear Regression are met.

NOTE:
Read data_description.txt to understand the house features more.

CREATORS:
Marc Medawar and Chase Sariaslani
