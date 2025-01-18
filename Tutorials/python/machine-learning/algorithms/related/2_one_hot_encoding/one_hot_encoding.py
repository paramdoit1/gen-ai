import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

le = LabelEncoder()

df = pd.read_csv('data/home_prices.csv')
#print(df)

dfle = df

dfle.town = le.fit_transform(dfle.town)
#print(dfle)

X = dfle[['town','area']].values
#print(X)

y = dfle.values

ct = ColumnTransformer([('town', OneHotEncoder(), [0])], remainder='passthrough')

X = ct.fit_transform(X)

X = X[:,1:]

print(X)

model = LinearRegression()
model.fit(X,y)

predict1 = model.predict([[0,1,3400]])
print('Predict1: ', predict1[0][2])

predict2 = model.predict([[1,0,2800]])
print('Predict2: ', predict2[0][2])