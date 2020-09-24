library(VIM)
library(dplyr)
library(car)
library(MASS)


#### AIC with cleaned file (no NAs) ####
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


#### Final EDA CSV file checking assumptions. ####
df2 = read.csv('EDA_final.csv')
# Convert Sales Price to log of sale price
df2$SalePrice = log(df2$SalePrice)

# Drop highly correlated columns (0.7 or higher) as found in Python.
df2 = subset(df2, select = -c(df2$TotalBsmtSF, df2$GrLivArea, df2$ExterQual, df2$FireplaceQu))

# Perform Multiple Linear Regression Assumptions
model = lm(formula=SalePrice ~ . - SalePrice , data=df2)
plot(model) # Assumptions look okay.
