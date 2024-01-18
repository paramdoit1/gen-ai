import pandas as pd

import os
print(os.getcwd())

df = pd.read_csv("data/movies.csv")

# Getting top 6 rows
print("The top 5 rows are : \n", df.head(5))

# Getting data shape
print("Data shape is : \n", df.shape)

# Getting column list
print("Column list: \n", df.columns)

# Getting unique data for column industry
print("Industry list: \n", df['industry'].unique())

# Getting unique data for column Language
print("Language list: \n", df.language.unique())

#Getting data count by industry
print("Industry Count: \n", df['industry'].value_counts())

#Getting data count by Language
print("Data count by Language: \n", df.language.value_counts())

#Getting movies released between 2000 and 2010
print(df[(df.release_year >= 2000) & (df.release_year <= 2010)])

#Getting movies released by specific studio
print(df[df.studio == 'Marvel Studios'])

#Getting details of numerical fields
print(df.describe())

#Getting details of all columns
print(df.info())

#Getting movie details of max and min imdb rating
print(df[(df.imdb_rating == df.imdb_rating.min()) | (df.imdb_rating == df.imdb_rating.max())])

#Adding age details based release year
df['age'] = df.release_year.apply(lambda x: 2024 -x)
print(df.age)

#Adding profit column based on revenue and budget
df['profit'] = df.apply(lambda x: x.revenue -x.budget, axis=1)
print(df.profit)

#Getting 3 columns of df
print(df[['title', 'age', 'profit']])

#Setting Title as index
df.set_index('title', inplace=True)

#Getting row details of specific rows
print(df.loc[['Pather Panchali', 'Pather Panchali']])

print(df.iloc[0])

df.reset_index(inplace=True)

print(df)
