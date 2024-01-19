import pandas as pd
import numpy as np

df = pd.read_csv('data/weather_by_cities.csv')

#Group data by city to create 3 groupby dataframes
df1 = df.groupby('city')

#City is key and other data is the value
for city, data in df1:
    print("City: ", city)
    print('Max Temperature: ', data.temperature.max())

#Max of each data in group
print(df1.max())

#Min of each data in group
print(df1.min())

#When min or max any method is executed in dataframe, it does 3 functions like split, 
# apply and combine.

#Describing the numerical field
print(df1.describe())

#getting size of each column
print(df1.size())

def grouper(df, col, idx):
    if(80 <= df[col].loc[idx] <=90):
        return "80-90"
    elif(50 <=df[col].loc[idx]<=70):
        return '50-70'
    else:
        return "Others"

df2 = df.groupby(lambda idx: grouper(df, 'temperature', idx))

for key, data in df2:
    print("key : ", key)
    print('Data: ', data)