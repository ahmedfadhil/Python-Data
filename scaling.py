import pandas as pd
import numpy as np

df = pd.DataFrame([
    'A+',
    'A',
    'A-',
    'B+',
    'B',
    'B-',
    'C+',
    'C',
    'C-',
    'D+',
    'D'
], index=[
    'Excellent',
    'Excellent',
    'Excellent',
    'Good',
    'Good',
    'Good',
    'Ok',
    'Ok',
    'Ok',
    'Poor',
    'Poor'
])

df.rename(columns={0: 'Grades'}, inplace=True)
print(df['Grades'].astype('category').head())

grades = df['Grades'].astype('category', categories=[
    'D',
    'D+',
    'C-',
    'C',
    'C+',
    'B-',
    'B',
    'B+',
    'A-',
    'A',
    'A+',
], ordered=True)

print(grades.head())
print(grades>'D')
