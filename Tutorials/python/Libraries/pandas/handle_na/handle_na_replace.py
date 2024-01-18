import pandas as pd
import numpy as np

df = pd.read_csv('data/weather_data_repl.csv')

#Specify  specific values to be replaced by nan
df1 = df.replace([-99999, -88888], value=np.nan)
print(df1)

#Specify column specific values to be replaced by nan
df2 = df.replace({
    'temperature': -99999,
    'windspeed': [-99999, -88888],
    'event':'no event'
}, np.nan)
print(df2)

#Specify old and new value
df3 = df.replace({
     -99999 : np.nan,
    -88888 : np.nan,
    'no event': 'sunny'
})
print(df3)

df4 = pd.DataFrame({
    'student' : ['Raju', 'Rama', 'Kiran'],
    'Grade':['exceptional', 'Good', 'Very Good']
})

df5 = df4.replace(['exceptional', 'Good', 'Very Good'], [5, 3, 4])
print(df5)