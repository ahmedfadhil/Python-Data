import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.DataFrame({'xx4': 'xx',
                   'xx5': 'xx',
                   'xx1': 'xx',
                   'xx2': 'xx',
                   })

df['Date'] = ['Decembner', 'January', 'midmay']

df['Delivery'] = True

df['feeds'] = ['postive', None, 'negative']
adf = df.reset_index()
adf['Date'] = pd.Series({0: 'decemner',
                         1: 'midmay'})


