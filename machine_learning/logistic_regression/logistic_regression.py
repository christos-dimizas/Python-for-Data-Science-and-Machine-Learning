# ------------------------------------------------------------ #
#       ------ Logistic Regression ------                      #
# ------------------------------------------------------------ #


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('titanic_train.csv')

# ------------------------------------------------------------ #
# basic data info
# ------------------------------------------------------------ #

print('')
print('-----------------------------------------')
print('Data (first rows)')
print('')
print(train.head())

print('')
print('-----------------------------------------')
print('Data columns')
print('')
print(train.columns)

# Lets check for nulls
print('')
print('-----------------------------------------')
print('HeatMap for nulls')
print('')
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis') \
    .set_title("HeatMap for nulls")
plt.show()

# Count Plot for Survived people per gender
print('')
print('-----------------------------------------')
print('Count Plot for Survived people per gender')
print('')
sns.countplot(x='Survived', hue='Sex', data=train) \
    .set_title("Count Plot for Survived people per gender")
plt.show()

# Distribution Plot for Age
print('')
print('-----------------------------------------')
print('Distribution Plot for Age')
print('')
sns.distplot(train['Age'].dropna(), kde=False, bins=30) \
    .set_title("Distribution Plot for Age")
plt.show()

# Box Plot for Pclass and Age
# 1st and 2nd class are older than people on 3rd class
print('')
print('-----------------------------------------')
print('Box Plot for Pclass and Age')
print('')
sns.boxplot(x='Pclass', y='Age', data=train) \
    .set_title("Box Plot for Pclass and Age")
plt.show()


# This function will replace the null values with values taken by the mean age of each Pclass case.
# NOTE: those values where picked by hand just from observing the box plots.
def impute_age(cols):
    age = cols[0]
    p_class = cols[1]

    if pd.isnull(age):
        if p_class == 1:
            return 37
        elif p_class == 2:
            return 29
        else:
            return 24
    else:
        return age


#  So, the train set will be transformed into:
train['Age'] = train[['Age', 'Pclass']].apply(impute_age, axis=1)

# Lets check for nulls again after we replaced them with mean values taken after observation
print('')
print('-----------------------------------------')
print('Lets check for nulls again after we replaced null ages with mean values taken after observation')
print('')
sns.heatmap(train.isnull(), yticklabels=False, cbar=False, cmap='viridis') \
    .set_title("HeatMap for nulls after we replaced null ages with mean values taken after observation")
plt.show()
