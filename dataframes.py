import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

p1 = pd.Series({'name': 'chris',
                'item': 'dog',
                'cost': 22.50})
p2 = pd.Series({'name': 'james',
                'item': 'cat',
                'cost': 25.50})
p3 = pd.Series({'name': 'john',
                'item': 'bird',
                'cost': 22.00})

df = pd.DataFrame([p1, p2, p3], index=['store1', 'store1', 'store3'])

print(df.head())

retrived = df.loc['store1', 'cost']

print('-------------')
print(retrived)
xy = df.T.loc['cost']

whack = df.loc['store1']['cost']

df.drop('store1')
# print(df)

copy_df = df.copy()
copy_df = copy_df.drop('store1')
# print(copy_df)
del copy_df['name']
# print(copy_df)

df['location'] = None

costs = df['cost']
# print(costs)

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
print(df.head())

plt.show()

for col in df.columns:
    if col[:2] == '01':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)

    if col[:2] == '02':
        df.rename(columns={col: 'Silver' + col[4:]}, inplace=True)

    if col[:2] == '03':
        df.rename(columns={col: 'Gold' + col[4:]}, inplace=True)
    if col[:2] == '№':
        df.rename(columns={col: '#' + col[4:]}, inplace=True)
print(df.head())

print(df['Gold'] > 0)

only_gold = df.where(df['Gold'] > 0)
only_gold.head()

goldy = only_gold['Gold'].count()

diga = df['Gold'].count()

only_gold = df[df['Gold'] > 0]
only_gold.head()

len(df[(df['Gold'] > 0) | df['Gold.1'] > 0])
dataframe = df[(df['Gold.1'] > 0) & df['Gold'] == 0]

df['country'] = df.index()
df = df.set_index('Gold')
df.head()

df = df.reset_index()
df.head()


