import numpy as np
import pandas as pd

df = pd.read_csv('./data/income.csv', names=['name','income'],skiprows=[0])

df_income_std_dev= np.std(df.income)
print('Standard deviation: ', df_income_std_dev)

#Geting 99 percentile
percentile_99= df.income.quantile(.99)
print('Percentile 99: ',percentile_99)
#Percentile 99:  9400479.999999994

#Removing outlier
df_no_outlier = df[df.income<=percentile_99]

#Standard Deviation
df_no_outlier_income_std_dev= np.std(df_no_outlier.income)
print('Standard deviation: ', df_no_outlier_income_std_dev)
# Standard deviation:  1406.8285846778444

# variance
df_no_outlier_income_var= np.var(df_no_outlier.income)
print('Variance: ', df_no_outlier_income_var)
#Variance:  1979166.6666666667