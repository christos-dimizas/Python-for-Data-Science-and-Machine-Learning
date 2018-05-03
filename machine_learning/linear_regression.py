# ------------------------------------------------------------ #
#       ------ Linear Regression ------                        #
# ------------------------------------------------------------ #


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------ #
# basic data info and plots
# ------------------------------------------------------------ #

USAhousing = pd.read_csv('USA_Housing.csv')
print('')
print('-----------------------------------------')
print('Data (first rows)')
print('')
print(USAhousing.head())
print('')
print('-----------------------------------------')
print('Data basic info')
print('')
print(USAhousing.info())
# Multi plots
sns.pairplot(USAhousing)
plt.show()

# Price distribution
sns.distplot(USAhousing['Price'])
plt.show()

# Heat map correlation between columns
sns.heatmap(USAhousing.corr(), annot=True)
plt.show()


# ------------------------------------------------------------ #
# Linear Regression Model
# ------------------------------------------------------------ #

# Our linear prediction will be on Price with all other fields be our variables. So:
# All available data columns are:
print('')
print('-----------------------------------------')
print('Data available columns')
print('')
print(USAhousing.columns)

# Which result to:
# Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
#        'Avg. Area Number of Bedrooms', 'Area Population', 'Price', 'Address'],
#       dtype='object')
# So X variables for our model will be:
X = USAhousing[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population']]
# With prediction variable the price
y = USAhousing['Price']
# First separate our data set into a training set and a test set.
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

# Next step is to create and train the model

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train, y_train)

print(lm.coef_)
# Lets now create a data frame which will show the linear model predicted coefficients
# Those coefficients are related to X columns and they express ratios between each X column and price
# In other words, one unit of increase of a X column value represents an increase of price relative to the related
# linear model coefficient.
cdf = pd.DataFrame(lm.coef_, X.columns, columns=['Coef'])
print('')
print('-----------------------------------------')
print('Linear model predicted coefficients')
print('')
print(cdf)


# ------------------------------------------------------------ #
# Linear Regression Predictions
# ------------------------------------------------------------ #

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.show()

sns.distplot(y_test - predictions)
plt.show()

# Basic distribution metrics
from sklearn import metrics
print('')
print('-----------------------------------------')
print('Mean Absolute Error of our prediction')
print('')
print(metrics.mean_absolute_error(y_test, predictions))

print('')
print('-----------------------------------------')
print('Mean Squared Error of our prediction')
print('')
print(metrics.mean_squared_error(y_test, predictions))