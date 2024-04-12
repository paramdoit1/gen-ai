import pandas as pd

import os
print(os.getcwd())

df = pd.read_csv('data\home_prices.csv')
print(df)