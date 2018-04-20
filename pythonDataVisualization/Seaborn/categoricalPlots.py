# ------------------------------------------------------------ #
#       ------ Categorical Data Plots ------        #
#   Now let's discuss using seaborn to plot categorical data! There are a few main plot types for this:
#       - factorplot
#       - boxplot
#       - violinplot
#       - stripplot
#       - swarmplot
#       - rplot
#       - countplot
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

# ------------------------------------------------------------ #
# barplot and countplot
# ------------------------------------------------------------ #

# These very similar plots allow you to get aggregate data off a categorical feature in your data. barplot is a general
# plot that allows you to aggregate the categorical data based off some function, by default the mean:
sns.barplot(x='sex', y='total_bill', data=tips)
plt.show()
# You can change the estimator object to your own function, that converts a vector to a scalar:
sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std)
plt.show()

# ------------------------------------------------------------ #
# countplot
# ------------------------------------------------------------ #

# This is essentially the same as barplot except the estimator is explicitly counting the number of occurrences.
# Which is why we only pass the x value:
sns.countplot(x='sex', data=tips)
plt.show()

# ------------------------------------------------------------ #
# boxplot and violinplot
# ------------------------------------------------------------ #
# boxplots and violinplots are used to shown the distribution of categorical data. A box plot (or box-and-whisker plot)
# shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels
# of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of
# the distribution, except for points that are determined to be “outliers” using a method that is a function of the
# inter-quartile range.

sns.boxplot(x="day", y="total_bill", data=tips, palette='rainbow')
plt.show()
# Can do entire dataframe with orient='h'
sns.boxplot(data=tips, palette='rainbow', orient='h')
plt.show()
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips, palette="coolwarm")
plt.show()

# ------------------------------------------------------------ #
# violinplot
# ------------------------------------------------------------ #

# A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across
# several levels of one (or more) categorical variables such that those distributions can be compared.
# Unlike a box plot, in which all of the plot components correspond to actual datapoints, the violin plot features a
# kernel density estimation of the underlying distribution.
sns.violinplot(x="day", y="total_bill", data=tips, palette='rainbow')
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips, hue='sex', palette='Set1')
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips, hue='sex', dodge=True, palette='Set1')
plt.show()

# ------------------------------------------------------------ #
# stripplot and swarmplot
# ------------------------------------------------------------ #

# The stripplot will draw a scatterplot where one variable is categorical. A strip plot can be drawn on its own, but
# it is also a good complement to a box or violin plot in cases where you want to show all observations along with
# some representation of the underlying distribution.

# The swarmplot is similar to stripplot(), but the points are adjusted (only along the categorical axis) so that they
# don’t overlap. This gives a better representation of the distribution of values, although it does not scale as well
# to large numbers of observations (both in terms of the ability to show all the points and in terms of the computation
# needed to arrange them).

sns.stripplot(x="day", y="total_bill", data=tips)
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips,
              jitter=True)  # Jitter adds some noise just to make things more visible
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue='sex', palette='Set1')
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue='sex', palette='Set1', dodge=True)
plt.show()

sns.swarmplot(x="day", y="total_bill", data=tips)
plt.show()

sns.swarmplot(x="day", y="total_bill", hue='sex', data=tips, palette="Set1", dodge=True)
plt.show()

# ------------------------------------------------------------ #
# Combining Categorical Plots
# ------------------------------------------------------------ #

sns.violinplot(x="tip", y="day", data=tips, palette='rainbow')
plt.show()
sns.swarmplot(x="tip", y="day", data=tips, color='black', size=3)
plt.show()

# ------------------------------------------------------------ #
# factorplot
# ------------------------------------------------------------ #

# factorplot is the most general form of a categorical plot. It can take in a kind parameter to adjust the plot type:
sns.factorplot(x='sex',y='total_bill',data=tips,kind='bar')
plt.show()
plt.show()
