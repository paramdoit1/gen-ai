import pandas as pd

in_weather = pd.DataFrame({
    'city': ['Mumbai', 'Chennai', 'Coimbatore'],
    'temperature': [30, 32, 28],
    'humidity': [80, 70, 68]
});

#print(in_weather)

us_weather = pd.DataFrame({
    'city': ['New York', 'Phoenix', 'San Hose'],
    'temperature': [20, 36, 28],
    'humidity': [50, 70, 66]
});

#print(us_weather)

df1 = pd.concat([in_weather, us_weather], ignore_index=True)
print(df1)

#Group by Countries
df2 = pd.concat([in_weather, us_weather], keys=["India", 'United States'])
print(df2)

temp_df = pd.DataFrame({
    'city': ['Mumbai', 'Chennai', 'Coimbatore'],
    'temperature': [30, 32, 28]
}, index=[0,1,2])

hum_df= pd.DataFrame({
    'city': ['Coimbatore', 'Chennai'],
    'humidity': [50, 70]
}, index=[2, 1])

print(temp_df)

df3 = pd.concat([temp_df, hum_df],  axis=1)
print(df3)

temp_df1 = pd.DataFrame({
    'city': ['Mumbai', 'Chennai', 'Coimbatore', 'Bangalore'],
    'temperature': [30, 32, 28, 26]
})

hum_df1 = pd.DataFrame({
    'city': ['Mumbai', 'Chennai', 'Coimbatore', 'Kochi'],
    'humidity': [51, 71, 61, 43]
})

#Inner join, show the data which is common
df4 = pd.merge(temp_df1, hum_df1, on='city')
print(df4)

#Left join, show the all data which is in left
df5 = pd.merge(temp_df1, hum_df1, on='city', how="left")
print(df5)

#right join, show the all data which is in right
df6 = pd.merge(temp_df1, hum_df1, on='city', how = "right")
print(df6)

#right join, show the all data which is in Outer
df7 = pd.merge(temp_df1, hum_df1, on='city', how = "outer")
print(df7)