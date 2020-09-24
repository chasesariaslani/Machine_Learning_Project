import pandas as pd
# To take into account relative file path
import os


# Locates EDA_Cleaned.csv in your current working directory
cwd_w_folder = os.path.abspath(os.path.dirname(__file__))
file_name = os.path.join(cwd_w_folder, 'EDA_Cleaned.csv')

#### Column Modifications ####

# house_features will be modified to allow easier encoding in Machine Learning

house_features = pd.read_csv(file_name)  # Taken after removing na's in R.
house_features = house_features.iloc[:, 1:]  # Removes ID column unnecessarily added by R.

## Neighbor and Exterior Modifications ##
# Use link before to find reasoning.
# https://www.gvdrenovationsinc.com/blog/the-5-most-popular-types-of-house-siding/
# Most used types of coverings is in this website.

# We will be categorizing them due to poor dummification.

# Exterior1st and Exterior2nd #
# Categories:
# 'VinylSd', 'MetalSd', 'Wd Sdng', 'HdBoard', 'BrkFace', 'WdShing',
# 'CemntBd', 'Plywood', 'AsbShng', 'Stucco', 'BrkComm', 'AsphShn',
# 'Stone', 'ImStucc', 'CBlock'

def exterior_categorizer(column):
    ''' Takes in dataframe coulmn and returns bins of exterior finish.
        Input: DataFrame Column
        Returns: Binned Column
    '''
    name = column.name
    vinyl = ['VinylSd']
    wood = ['Wd Sdng', 'HdBoard', 'WdShing', 'Plywood']
    metal = ['MetalSd']
    cement = ['CemntBd', 'AsbShng', 'CBlock', 'PreCast']
    stucco = ['Stucco', 'ImStucc']
    brick = ['BrkFace', 'BrkComm', 'AsphShn']
    stone = ['Stone']
    exterior_column = []

    for item in column:
        if item in vinyl:
            exterior_column.append('Vinyl')
        elif item in wood:
            exterior_column.append('Wood')
        elif item in metal:
            exterior_column.append('Metal')
        elif item in cement:
            exterior_column.append('Cement')
        elif item in stucco:
            exterior_column.append('Stucco')
        elif item in brick:
            exterior_column.append('Brick')
        elif item in stone:
            exterior_column.append('Stone')
        else:
            exterior_column.append('Other')
    return(pd.DataFrame({name: exterior_column}))


exterior_1st_column = exterior_categorizer(house_features['Exterior1st'])
exterior_2nd_column = exterior_categorizer(house_features['Exterior2nd'])

## Neighborhood Modification
# Binning neighborhood based on cardinal location.
north = ['NoRidge', 'Somerst', 'NWAmes', 'Blmngtn', 'NridgHt',
         'NAmes', 'Gilbert', 'StoneBr', 'NPkVill', 'BrDale']
east = ['OldTown', 'BrkSide', 'IDOTRR']
south = ['Mitchel', 'MeadowV', 'Timber']
west = ['CollgCr', 'Sawyer', 'SawyerW', 'ClearCr']
center = ['Veenker', 'Crawfor', 'Edwards', 'SWISU', 'Blueste']
neighborhood_column = []

for neighborhood in house_features['Neighborhood']:
    if neighborhood in north:
        neighborhood_column.append('North')
    elif neighborhood in east:
        neighborhood_column.append('East')
    elif neighborhood in south:
        neighborhood_column.append('South')
    elif neighborhood in west:
        neighborhood_column.append('West')
    elif neighborhood in center:
        neighborhood_column.append('Center')

house_features['Neighborhood'] = neighborhood_column


## MasVnrArea and GarageYrBlt modification ##
house_features['MasVnrArea'].replace({'None': 0}, inplace=True)
house_features['MasVnrArea'] = house_features['MasVnrArea'].astype('int64')
house_features['GarageYrBlt'].replace({'None': 0}, inplace=True)
house_features['GarageYrBlt'] = house_features['GarageYrBlt'].astype('int64')

## Segregating the DataFrame##
# We need to segregate the dataframes to make it easier for dummification.

# Nomimal Variables:
nominal = house_features[['MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour',
                          'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
                          'Condition2', 'HouseStyle', 'RoofStyle', 'RoofMatl',
                          'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Foundation', 'Heating',
                          'CentralAir', 'Electrical', 'GarageType', 'PavedDrive', 'MiscFeature',
                          'SaleType', 'SaleCondition', 'BldgType', 'BsmtFinType1', 'BsmtFinType2',
                          'GarageFinish', 'Functional', 'Fence']]

# Ordinal Variables:
ordinal = house_features[['ExterQual', 'ExterCond', 'BsmtQual',
                          'BsmtCond', 'BsmtExposure', 'HeatingQC', 'KitchenQual', 
                          'FireplaceQu', 'GarageQual', 'GarageCond']]

# Numeric Variables:
numeric = house_features.loc[:, house_features.dtypes == "int64"]


# Ordinal has categorical variables that can be changed to numeric. 0 is Poor quality or None 4 is exceelent quality.
ordinal['ExterQual'] = ordinal['ExterQual'].map({'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['ExterCond'] = ordinal['ExterCond'].map({'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['BsmtQual'] = ordinal['BsmtQual'].map({'None':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['BsmtCond'] = ordinal['BsmtCond'].map({'None':0,'Po':0,'Fa':1,'TA':2,'Gd':3})
ordinal['BsmtExposure'] = ordinal['BsmtExposure'].map({'None':0,'No':0,'Mn':1,'Av':2,'Gd':3})
ordinal['HeatingQC'] = ordinal['HeatingQC'].map({'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['KitchenQual'] = ordinal['KitchenQual'].map({'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['FireplaceQu'] = ordinal['FireplaceQu'].map({'None':0,'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['GarageQual'] = ordinal['GarageQual'].map({'None':0,'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})
ordinal['GarageCond'] = ordinal['GarageCond'].map({'None':0,'Po':0,'Fa':1,'TA':2,'Gd':3,'Ex':4})


## Predictor Variable: ##
sale_price = house_features['SalePrice']


### Writing CSV file to current Folder ###
final_file_name = os.path.join(cwd_w_folder, 'EDA_final.csv')
sale_price_file_name = os.path.join(cwd_w_folder, 'SalePrice_final.csv')
nominal_file_name = os.path.join(cwd_w_folder, 'Nominal.csv')
ordinal_file_name = os.path.join(cwd_w_folder, 'Ordinal.csv')
numeric_file_name = os.path.join(cwd_w_folder, 'Numeric.csv')
house_features.to_csv(final_file_name, encoding='utf-8', index=False)
sale_price.to_csv(sale_price_file_name, encoding='utf-8', index=False)
nominal.to_csv(nominal_file_name, encoding='utf-8', index=False)
ordinal.to_csv(ordinal_file_name, encoding='utf-8', index=False)
numeric.to_csv(numeric_file_name, encoding='utf-8', index=False)
