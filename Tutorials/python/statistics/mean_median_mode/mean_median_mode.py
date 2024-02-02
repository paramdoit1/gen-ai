import numpy as np
import pandas as pd

df = pd.read_csv('./data/income.csv', names=['name','income'],skiprows=[0])

#Getting the statistics of numeric column of income
print(df.describe())
'''
       income
count  7.000000e+00
mean   1.433929e+06
std    3.777283e+06
min    4.000000e+03
25%    5.500000e+03
50%    7.000000e+03
75%    7.750000e+03
max    1.000000e+07

'''
#Geting seventy fifth quantile
percentile_75= df.income.quantile(.75)
print('Percentile 75: ',percentile_75)
#Percentile 75:  7750.0

#Geting 99 percentile
percentile_99= df.income.quantile(.99)
print('Percentile 99: ',percentile_99)
#Percentile 99:  9400479.999999994

#Removing outlier
df_no_outlier = df[df.income<=percentile_99]
print(df_no_outlier)

#Getting mean
df_income_mean = df_no_outlier.income.mean()
print('Income mean: ',df_income_mean)
#Income mean:  6250.0

#Getting Median
df_income_median = df_no_outlier.income.median()
print('Income median: ',df_income_median)
#Income median:  6500.0

#Getting mode
df_income_mode = df_no_outlier.income.mode()
print('Income Mode: ',df_income_mode)
#Income Mode:  0    4000
