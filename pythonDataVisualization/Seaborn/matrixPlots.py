# ------------------------------------------------------------ #
#        ------ Matrix Plots ------      #
# Matrix plots allow you to plot data as color-encoded matrices
# and can also be used to indicate clusters within the data
# (later in the machine learning section we will learn how to
# formally cluster data).
# ------------------------------------------------------------ #

import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')

# ------------------------------------------------------------ #
# Heatmap
# ------------------------------------------------------------ #

# In order for a heatmap to work properly, your data should already be in a matrix form, the sns.heatmap
# function basically just colors it in for you
# To convert flight data to matrix we can do:

pvflights = flights.pivot_table(values='passengers', index='month', columns='year')

sns.heatmap(pvflights)
plt.show()

sns.heatmap(pvflights, cmap='magma', linecolor='white', linewidths=1)
plt.show()

# ------------------------------------------------------------ #
# clustermap
# ------------------------------------------------------------ #

# The clustermap uses hierarchal clustering to produce a clustered version of the heatmap.

# Notice now how the years and months are no longer in order, instead they are grouped by similarity in value
# (passenger count). That means we can begin to infer things from this plot, such as August and July being similar
# (makes sense, since they are both summer travel months)

sns.clustermap(pvflights)
plt.show()

# More options to get the information a little clearer like normalization
sns.clustermap(pvflights, cmap='coolwarm', standard_scale=1)
plt.show()
