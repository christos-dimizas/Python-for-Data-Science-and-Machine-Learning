# ------------------------------------------------------------ #
#        ------ Grids ------      #
# Grids are general types of plots that allow you to map plot
# types to rows and columns of a grid, this helps you create
# similar plots separated by features.
# ------------------------------------------------------------ #


import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

# ------------------------------------------------------------ #
# PairGrid
# ------------------------------------------------------------ #

# Pairgrid is a subplot grid for plotting pairwise relationships in a dataset.
# Just the Grid
sns.PairGrid(iris)

# Then you map to the grid# Then y
g1 = sns.PairGrid(iris)
g1.map(plt.scatter)
plt.show()

# Map to upper,lower, and diagonal# Map to
g2 = sns.PairGrid(iris)
g2.map_diag(plt.hist)
g2.map_upper(plt.scatter)
g2.map_lower(sns.kdeplot)
plt.show()

# ------------------------------------------------------------ #
# pairplot
# ------------------------------------------------------------ #

# pairplot is a simpler version of PairGrid (you'll use quite often)
sns.pairplot(iris)
plt.show()

sns.pairplot(iris, hue='species', palette='rainbow')
plt.show()

# ------------------------------------------------------------ #
# Facet Grid
# ------------------------------------------------------------ #

# FacetGrid is the general way to create grids of plots based off of a feature:

tips = sns.load_dataset('tips')
# Just the Grid
g3 = sns.FacetGrid(tips, col="time", row="smoker")
g3 = g3.map(plt.hist, "total_bill")
plt.show()

g4 = sns.FacetGrid(tips, col="time",  row="smoker",hue='sex')
# Notice hwo the arguments come after plt.scatter call
g4 = g4.map(plt.scatter, "total_bill", "tip").add_legend()
plt.show()


# ------------------------------------------------------------ #
# JointGrid
# ------------------------------------------------------------ #

# JointGrid is the general version for jointplot() type grids, for a quick example:

g5 = sns.JointGrid(x="total_bill", y="tip", data=tips)
g5 = g5.plot(sns.regplot, sns.distplot)
plt.show()


