library(VIM)
library(dplyr)
library(car)
library(MASS)

df = read.csv('EDA_Cleaned.CSV', stringsAsFactors = FALSE) # Set to WD

df = subset(df, select = -c(X)) # Removes X


model.empty = lm(log(SalePrice) ~ 1, data = df)
model.full = lm(log(SalePrice) ~ ., data = df)
scope = list(lower = formula(model.empty), upper = formula(model.full))

#Stepwise regression using AIC as the criteria (the penalty k = 79).

forwardAIC = step(model.empty, scope, direction = "forward", k = 79) # This one is quick.
summary(forwardAIC)
# When doing forward AIC, got this conclusion:
# R-squared:  0.8365
# SalePrice ~ OverallQual + GrLivArea + YearBuilt + OverallCond + GarageCars + TotalBsmtSF




backwardAIC = step(model.full, scope, direction = "backward", k = 79) # This one will destroy your computer.
summary(backwardAIC)
# When doing backwardAIC, Got this conclusion:
# R-squared:  0.843
# SalePrice ~ OverallQual + OverallCond + YearBuilt + X1stFlrSF + X2ndFlrSF + BsmtFullBath + GarageCars