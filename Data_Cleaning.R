library(tidyverse)

# Please read from same directory.
df = read.csv('train.csv', stringsAsFactors = FALSE) %>%
  select(-Id)  # Removes ID. its an unnecessary index

missing = colnames(df)[colSums(is.na(df)) > 0] # finds the columns with missing values.

######################################################################
# Use this piece of code to find the percentage missing:

#t = c()
#k=1
#for (x in MISSING){
#  t[k] = round(sum(is.na(df[,x]))/nrow(df),4) *100
#  print( paste(x,' ', sum(is.na(df[,x])),' ', round(sum(is.na(df[,x]))/nrow(df),3) *100,'%',sep = ''))
#  k = k+1
#}
#t

# Create Data Frame for plot look.

#temp = data.frame('col_missing' = MISSING,'count_percent'=t)%>% 
#  arrange(desc(count_percent)) # sorts missing data

#temp

# ggplot percentage of missingness chart.

#temp %>% 
#  arrange(.,desc(count_percent)) %>%
#  head(6) %>% # Omitting other columns since the percentage of each variable's missingness is less than 5%
#  ggplot(aes(x=reorder(col_missing,-count_percent),y=count_percent)) + 
#  geom_col(aes( fill=col_missing)) + 
#  theme(legend.position = "none",axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1)) +
#  labs (x = "Feature",
#        y = "% of missingness",
#        title = "Percentage of Missingness per Feature") # + ggsave('missingness_percentage.png')
######################################################################

## Data Cleaning ##
# Pool Quality Modification.
pool_column = select(df, PoolQC)
pool_column[is.na(pool_column)] = 0 # No Pool
pool_column[pool_column =='Ex'] = 3 # Excellent Pool
pool_column[pool_column =='Gd'] = 2 # Good Pool
pool_column[pool_column =='Fa'] = 1 # Fair Pool
df = subset(df, select=c(-PoolQC))
df = cbind(df, pool_column) # Replaces PoolQC with the discrete representation of Pool Quality. Run this only once


# Adding "None" to many columns where NA means none.
df$MiscFeature[is.na(df$MiscFeature)] = 'None'
df$Alley[is.na(df$Alley)] = 'None'
df$Fence[is.na(df$Fence)] = 'None'
df$FireplaceQu[is.na(df$FireplaceQu)] = 'None'
df$GarageType[is.na(df$GarageType)] = 'None'
df$GarageYrBlt[is.na(df$GarageYrBlt)] = 'None'
df$GarageCond[is.na(df$GarageCond)] = 'None'
df$GarageFinish[is.na(df$GarageFinish)] = 'None'
df$GarageQual[is.na(df$GarageQual)] = 'None'
df$BsmtExposure[is.na(df$BsmtExposure)] = 'None'
df$BsmtFinType2[is.na(df$BsmtFinType2)] = 'None'
df$BsmtQual[is.na(df$BsmtQual)] = 'None'
df$BsmtCond[is.na(df$BsmtCond)] = 'None'
df$BsmtFinType1[is.na(df$BsmtFinType1)] = 'None'
df$MasVnrType[is.na(df$MasVnrType)] = 'None'
df$MasVnrArea[is.na(df$MasVnrArea)] = 'None'

# Impute median for LotFrontage.
m = median(df$LotFrontage,na.rm = T)
df$LotFrontage[is.na(df$LotFrontage)] = m

# Because we only have one missing value we replace it by the mode.
df$Electrical[is.na(df$Electrical)] = 'SBrkr'

#################################################################
# Checks if there are any missing values left in dataframe.

# sum(is.na(df)) # There are no more empty values.
#################################################################


## Write to CSV
write.csv(df, file='EDA_Cleaned.csv') 