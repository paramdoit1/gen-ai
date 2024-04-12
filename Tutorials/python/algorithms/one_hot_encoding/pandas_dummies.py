import pandas as pd
from sklearn.linear_model import LinearRegression

import os
print(os.getcwd())

df = pd.read_csv('data/home_prices.csv')
#print(df)

dummies = pd.get_dummies(df.town)
#print(dummies)

merged = pd.concat([df,dummies], axis='columns')
#print(merged)

final = merged.drop(['town'], axis='columns')
#print(final)

final = final.drop(['west windsor'], axis='columns')
#print(final)

X = final.drop('price', axis='columns')
print(X)

y=final.price

model = LinearRegression()

model.fit(X,y)

predict_values = model.predict(X)
print(predict_values)

score= model.score(X,y)
print(score)

predict1 = model.predict([[3400, 0 ,0]])
print('predict1', predict1)
