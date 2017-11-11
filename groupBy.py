import pandas as pd
import numpy as np

df = pd.read_csv('census.csv')
df = df[df['SUMLEV'] == 50]
# Using the unique() method
# for state in df['STNAME'].unique():
#     avg = np.average(df.where(df['STNAME'] == state).dropna()['CENSUS2010POP'])
#     print('Countries in state ' + state + ' have an average of ' + str(avg))

# Using the groupby method
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    # print('Countries in state ' + group + ' have an average of ' + str(avg))

df = df.set_index('STNAME')


def fun(item):
    if item < 'M':
        return 0
    if item < 'Q':
        return 1
    return 2


for group, frame in df.groupby(fun):
    # print('There are ' + str(len(frame)) + ' records in processing' + str(group) + 'for processiing.')
    pass
whackit = df.groupby('STNAME').agg({'CENSUS2010POP': np.average})
# print(whackit)

print(type(df.groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011']))
print()
print(type(df.groupby(level=0)['POPESTIMATE2010']))

# Using groupby in DataFrame
(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({
    'AVG': np.average,
    'SUM': np.sum
}))

# Using groupby in Series
(df.set_index('STNAME').groupby(level=0)['POPESTIMATE2010', 'POPESTIMATE2011'].agg(
    {
        'av': np.average,
        'su': np.sum
    }))

#
# print(df.head())
