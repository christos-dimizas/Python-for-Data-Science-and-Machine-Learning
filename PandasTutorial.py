import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
#   -- Dictionary
d = {'a': 10, 'b': 20, 'c': 30}

# ------------------------------------------------------------ #
# --------- SERIES ------------------------------------------- #
# ------------------------------------------------------------ #

#   -- A Series can also include functions as a reference.
pd.Series(data=labels)
pd.Series(data=my_data, index=labels)
pd.Series(arr, index=labels)
pd.Series(d)

# ------------------------------------------------------------ #
# --------- DataFrames --------------------------------------- #
# ------------------------------------------------------------ #
# (matrix)
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# print(df, '\n \n', df['W'], ' \n \n ', df[['W', 'Z']])
df['new'] = df['W'] + df['Z']
#   -- Drop column
df.drop('new', axis=1, inplace=True)
#   -- Drop line (with the inplace the data is not actually deleted)
df.drop('E', axis=0)
#   -- Select rows and columns
# print(df.loc[['A', 'B'], ['W', 'Y']])

#   -- Conditional Selection
# print(df[(df['W'] > 0) & (df['Y'] > 1)]['X'])
# print(df[(df['W'] > 0) | (df['Y'] > 1)]['X'])

# ------------------------------------------------------------ #
# --------- GroupBy ------------------------------------------ #
# ------------------------------------------------------------ #
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2', ]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))  # this creates tuple pairs
hier_index = pd.MultiIndex.from_tuples(hier_index)

df2 = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
df2.index.names = ['Groups', 'Num']
#   -- Select a value
# print(df2.loc['G2'].loc[2]['A'])

#   -- Cross Section method for multi selection of Num = 1 on both groups
# print(df2.xs(1, level='Num'))

#   -- GROUP BY AND APPLY A METHON ON IT
#   -- Create dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df3 = pd.DataFrame(data)
# print(df3.groupby('Company').describe().transpose()['FB'])


# ------------------------------------------------------------ #
# --------- MERGING, JOINING AND CONCATENATING --------------- #
# ------------------------------------------------------------ #
df_a = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df_b = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                     'B': ['B4', 'B5', 'B6', 'B7'],
                     'C': ['C4', 'C5', 'C6', 'C7'],
                     'D': ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

df_c = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                     'B': ['B8', 'B9', 'B10', 'B11'],
                     'C': ['C8', 'C9', 'C10', 'C11'],
                     'D': ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

#   -- Concatenation works when the data concat axis dimensions are the same.
#   -- Otherwise we will get NaN values.
#   -- Concat rows - WORKS
# print(pd.concat([df_a, df_b, df_c]))
#   -- Concat columns - DOESN'T WORKS
# print(pd.concat([df_a, df_b, df_c], axis=1))

#   -- Merging
#   -- The merge function allows you to merge DataFrames together using a similar logic as merging SQL Tables together
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

# print(pd.merge(left, right, how='inner', on='key'))

#   -- Joining
#   -- Joining is a convenient method for combining the columns of two potentially differently-indexed DataFrames into a
#       single result DataFrame.
left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                       'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])
# print(left2.join(right2))


# ------------------------------------------------------------ #
# --------- Data Input & Output ------------------------------ #
# ------------------------------------------------------------ #

#   Four libraries are required (sqlalchemy, lxml, html5lib, BeautifulSoup4)
#   Read
df_file = pd.read_excel('./dataFiles/Excel_Sample.xlsx', sheet_name='Sheet1')
#   Save
# df_file.to_excel('Excel_Sample2.xlsx', sheet_name='my sheet')
# print(df_file)

#   HTML input
# df_html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')
# print(df_html[0].head())

#   SQL
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
df_file.to_sql('tableName', engine)
sql_df = pd.read_sql('tableName', con=engine)
print(sql_df)