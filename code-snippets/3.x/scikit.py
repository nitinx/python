# SECTION #1
# Code you have previously used to load data
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
#from sklearn.impute import SimpleImputer

from sklearn.preprocessing.imputation import Imputer

# Path of the file to read. We changed the directory structure to simplify submitting to a competition
iowa_file_path = '../input/train.csv'

train_data = pd.read_csv(iowa_file_path)

# Drop houses where the target is missing
#train_data.dropna(axis=0, subset=['BsmtQual'], inplace=True)
#train_data.drop(['MSSubClass'])

# Original Data
#missing_val_count_by_column = (train_data_original.isnull().sum())
#print(missing_val_count_by_column[missing_val_count_by_column > 0])

#my_imputer = Imputer()
#train_data = my_imputer.fit_transform(train_data_original)

# Imputed Data
print("Train Data:")
missing_val_count_by_column = (train_data.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

# Create target object and call it y
y = train_data.SalePrice
# Create X
# No categoricals | 22762
#features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd'] --> 22762

# No categoricals | 18287
'''features = ['LotArea', 'OverallQual', 'OverallCond', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'FullBath',
            'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'WoodDeckSF', 'ScreenPorch', 'PoolArea']'''

# With categoricals | 17846
features = ['LotArea', 'BldgType', 'OverallQual', 'OverallCond', 'YearBuilt', 'BsmtQual', '1stFlrSF', '2ndFlrSF',
            #'BsmtFullBath',
            'GrLivArea', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'WoodDeckSF',
            'ScreenPorch', 'PoolArea']


X_temp1 = train_data[features]
#X_temp1 = X_temp1.fillna(method='ffill')
X_temp2 = pd.get_dummies(X_temp1)
#X_temp2 = my_imputer.fit_transform(X_temp2)

test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)
#test_data = test_data.fillna(method='ffill')

print("Test Data:")
missing_val_count_by_column = (test_data.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

# Drop houses where the target is missing
#test_data.dropna(axis=0, subset=['BsmtQual'], inplace=True)
#test_data.drop(['MSSubClass'])

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
test_X_temp1 = test_data[features]
test_X_temp2 = pd.get_dummies(test_X_temp1)
#test_X_temp2 = my_imputer.fit_transform(test_X_temp2)

X, test_X = X_temp2.align(test_X_temp2, join='left', axis=1)

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

# Using best value for max_leaf_nodes
iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
iowa_model.fit(train_X, train_y)
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

train_data.dtypes.sample(50)

# SECTION #2
# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state=1)

# fit rf_model_on_full_data on all data from the
rf_model_on_full_data.fit(X, y)

# SECTION #3
# path to file you will use for predictions
#test_data_path = '../input/test.csv'

# read test data file using pandas
#test_data = pd.read_csv(test_data_path)

# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
#test_X_temp = test_data[features]
#test_X = pd.get_dummies(test_X_temp)

# make predictions which we will submit.
test_predictions = rf_model_on_full_data.predict(test_X)

# The lines below shows you how to save your data in the format needed to score it in the competition
output = pd.DataFrame({'Id': test_data.Id,
                       'SalePrice': test_predictions})

output.to_csv('../input/submission.csv', index=False)
