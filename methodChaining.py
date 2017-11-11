import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
# The Pandorable way
# (df.where(df['SUMLEV'] == 50)
#     .dropna()
#     .set_index(['STNAME', "CTYNAME"])
#     .rename(columns={
#     'ESTIMATESBASE2010': 'Estimates Base 2010'
# }))
# The classic way
df = df[df['SUMLEV'] == 50]
df.set_index(['STNAME', 'CTYNAME'], inplace=True)
df.rename(columns={
    'ESTIMATESBASE2010': 'Estimates Base 2010'
})
print(df['ESTIMATESBASE2010'])


def min_max(row):
    data = row[[
        'POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015',
    ]]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


df.apply(min_max, axis=1)

rows = [
    'POPESTIMATE2010',
    'POPESTIMATE2011',
    'POPESTIMATE2012',
    'POPESTIMATE2013',
    'POPESTIMATE2014',
    'POPESTIMATE2015',
]

df.apply(lambda x: np.max(x[rows]), axis=1)





















