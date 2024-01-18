import pandas as pd

df = pd.read_csv('data/weather_data.csv', parse_dates=['day'])

df.set_index("day", inplace=True)

#Fill all NaN with 0
df1 = df.fillna(0)
print(df1)

#Providing specific values based on column for NaN
df2 = df.fillna({
    'temperature': df.temperature.mean(),
    'windspeed': df.windspeed.mean(),
    'event': 'No Event'
})
print (df2)

#Fill with previous values for NaN
df3=df.fillna(method='ffill')
print(df3)

#Fill with Next values for NaN
df4=df.fillna(method='bfill')
print(df4)

#Fill with previous values for NaN with limit parameter
df5=df.fillna(method='ffill', limit=1)
print(df5)

#Getting linear increase
df6 = df.interpolate()
print(df6)

#Drop the rows with NaN
df7 = df.dropna()
print(df7)

#Drop the rows with NaN when all values are NaN
df8 = df.dropna(how="all")
print(df8)

#Set threshold of 2. drop only if there are 2 NAN in a row
df9 = df.dropna(thresh=2)
print(df9)