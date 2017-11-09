import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df.head()
print(df['SUMLEV'].unique())

df = df[df['SUMLEV'] == 50]

columns_to_keep = [
    'sdd',
    'sdd',
    'sdd',
    'sdd',
    'sdd',
    'sdd'
]

df = df[columns_to_keep]
df.head()

df = df.set_index(['STNAME', 'CTYNAME'])

comparing = df.loc[[('state', 'county'), ('another state', 'another county')]]

# df.fillna?


df = df.set('Time')
df = df.sort_index()















































