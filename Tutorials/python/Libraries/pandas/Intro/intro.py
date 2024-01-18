import pandas as pd

import os
print(os.getcwd())

df = pd.read_csv("data/movies.csv")

# Gettimg top 6 rows
print("The top 5 rows are : \n", df.head(5))

# Getting last 6 rows
print("The last 5 rows are : \n", df.tail(5))

#Random 4 rows
print("Random 4 rows: \n", df.sample(4))

#Getting rows 2 to 4
print("Getting rows 2 to 4: \n", df[2:5])

#Getting shape of data. count of rows and columns
print("Random Shape: \n", df.shape)

#Printing column data: imdb_rating
print("Getting column data: \n", df['imdb_rating'])

#Getting min imdb rating
print("Getting min imdb rating : \n", df['imdb_rating'].min())

#Getting max imdb rating
print("Getting max imdb rating : \n", df.imdb_rating.max())

#Getting mean imdb rating
print("Getting mean imdb rating : \n", df.imdb_rating.mean())

df_b =df[df.industry=='Bollywood']
df_h =df[df.industry=='Hollywood']

#Getting min, max, mean of bollywood

print("Getting min, max, mean imdb rating of bollywood: \n", df_b.imdb_rating.min(),  df_b.imdb_rating.max(),  df_b.imdb_rating.mean())
print("Getting min, max, mean imdb rating of Hollywood: \n", df_h.imdb_rating.min(),  df_h.imdb_rating.max(),  df_h.imdb_rating.mean())
