import pandas as pd
import numpy as np

# pd.Series?

animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = [1, 2, 3, 4, ]

objecting = pd.Series(numbers)
animals1 = ['Tiger', 'Bear', None]
number1 = [1, 2, 3, 4, None]
xyz = pd.Series(number1)

# patos = np.nan == None
patos = np.nan == np.nan
matos = np.isnan(np.nan)

sports = {
    'wa': 'kiki',
    'wa1': 'kiki1',
    'wa4': 'kiki5'
}

# s = pd.Series(sports)
# print(s.index)

s = pd.Series(['Tiger', 'mama', 'ksksk'], index=['1', '2', '33'])

print(s)
