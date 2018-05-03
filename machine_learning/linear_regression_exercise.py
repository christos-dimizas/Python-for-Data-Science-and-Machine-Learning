# ------------------------------------------------------------ #
# PROJECT EXERCISE
# ------------------------------------------------------------ #

# Get the Data
# We'll work with the Ecommerce Customers csv file from the company. It has Customer info, suchas Email, Address, and their color Avatar. Then it also has numerical value columns:
#
# Avg. Session Length: Average session of in-store style advice sessions.
# Time on App: Average time spent on App in minutes
# Time on Website: Average time spent on Website in minutes
# Length of Membership: How many years the customer has been a member.
# Read in the Ecommerce Customers csv file as a DataFrame called customers.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

customers = pd.read_csv("Ecommerce_Customers.csv")

print('')
print('-----------------------------------------')
print('Check the head of customers, and check out its info() and describe() methods')
print('')
print(customers.head())
print('')
print('')
print(customers.describe())
print('')
print('')
print(customers.info())

# Let's explore the data!
#
# For the rest of the exercise we'll only be using the numerical data of the csv file.
#
# Use seaborn to create a jointplot to compare the Time on Website and Yearly Amount Spent columns.
# Does the correlation make sense?

sns.set_palette('GnBu_d')
sns.set_style('whitegrid')
# More time on site, more money spent.
print('')
print('-----------------------------------------')
print('Show jointplot between "Time on Website" and "Yearly Amount Spent" plot')
print('')
sns.jointplot(x='Time on Website', y='Yearly Amount Spent', data=customers)
plt.show()

# Do the same but with the Time on App column instead.
print('')
print('-----------------------------------------')
print('Show jointplot between "Time on App" and "Yearly Amount Spent" plot')
print('')
sns.jointplot(x='Time on App', y='Yearly Amount Spent', data=customers)
plt.show()

# Use jointplot to create a 2D hex bin plot comparing Time on App and Length of Membership.
print('')
print('-----------------------------------------')
print('Show jointplot between "Time on App" and "Length of Membership" plot')
print('')
sns.jointplot(x='Time on App', y='Length of Membership', kind='hex', data=customers)
plt.show()

# Let's explore these types of relationships across the entire data set. Use pairplot to recreate the plot below.
print('')
print('-----------------------------------------')
print('Show pairplot plot to explore these types of relationships across the entire data set')
print('')
sns.pairplot(customers)
plt.show()

# Create a linear model plot (using seaborn's lmplot) of Yearly Amount Spent vs. Length of Membership.
print('')
print('-----------------------------------------')
print('Show linear model plot of x="Length of Membership", y="Yearly Amount Spent"')
print('')
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent', data=customers)
plt.show()

# ------------------------------------------------------------------ #
# Training and Testing Data
#
# Now that we've explored the data a bit, let's go ahead and split the data into training and testing sets.
# Set a variable X equal to the numerical features of the customers and
# a variable y equal to the "Yearly Amount Spent" column.

y = customers['Yearly Amount Spent']
X = customers[['Avg. Session Length', 'Time on App', 'Time on Website', 'Length of Membership']]

# Use model_selection.train_test_split from sklearn to split the data into training and testing sets.
# Set test_size=0.3 and random_state=101
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Training the Model
# Now its time to train our model on our training data!
#
# Import LinearRegression from sklearn.linear_model
from sklearn.linear_model import LinearRegression

# Create an instance of a LinearRegression() model named lm.
lm = LinearRegression()
# Train/fit lm on the training data.
lm.fit(X_train, y_train)
# The coefficients
print('')
print('-----------------------------------------')
print('The coefficients')
print('')
print('Coefficients: \n', lm.coef_)

# Predicting Test Data
# Now that we have fit our model, let's evaluate its performance by predicting off the test values!
#
# Use lm.predict() to predict off the X_test set of the data.
predictions = lm.predict(X_test)

# Create a scatterplot of the real test values versus the predicted values.
print('')
print('-----------------------------------------')
print('Create a scatterplot of the real test values versus the predicted values')
print('')
plt.scatter(y_test, predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()

# Evaluating the Model
# Let's evaluate our model performance by calculating the residual sum of squares and the
# explained variance score (R^2).
#
# Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error.
# Refer to the lecture or to Wikipedia for the formulas


# calculate these metrics by hand
from sklearn import metrics
print('')
print('-----------------------------------------')
print('Calculate the Mean Absolute Error, Mean Squared Error, and the Root Mean Squared Error')
print('')
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

# Residuals
# You should have gotten a very good model with a good fit. Let's quickly explore the residuals to make sure
# everything was okay with our data.
#
# Plot a histogram of the residuals and make sure it looks normally distributed.
# Use either seaborn distplot, or just plt.hist().
print('')
print('-----------------------------------------')
print('Plot a histogram of the residuals and make sure it looks normally distributed')
print('')
sns.distplot((y_test - predictions), bins=50)
plt.show()

# Conclusion
# We still want to figure out the answer to the original question, do we focus our effort on mobile app or
# website development? Or maybe that doesn't even really matter, and Membership Time is what is really important.
# Let's see if we can interpret the coefficients at all to get an idea.
#
# Recreate the dataframe below.
coefficients = pd.DataFrame(lm.coef_, X.columns)
coefficients.columns = ['Coefficient']
print('')
print('-----------------------------------------')
print('Coefficients')
print('')
print(coefficients)

# How can you interpret these coefficients?
#
# Interpreting the coefficients:
#
# Holding all other features fixed, a 1 unit increase in Avg. Session Length is associated with an increase of
# 25.98 total dollars spent.

# Holding all other features fixed, a 1 unit increase in Time on App is associated with an increase of
# 38.59 total dollars spent.

# Holding all other features fixed, a 1 unit increase in Time on Website is associated with an increase of
# 0.19 total dollars spent.

# Holding all other features fixed, a 1 unit increase in Length of Membership is associated with an increase of
# 61.27 total dollars spent.

# Do you think the company should focus more on their mobile app or on their website?
#
# This is tricky, there are two ways to think about this: Develop the Website to catch up to the performance
# of the mobile app, or develop the app more since that is what is working better.
# This sort of answer really depends on the other factors going on at the company, you would probably want to
# explore the relationship between Length of Membership and the App or the Website before coming to a conclusion!
