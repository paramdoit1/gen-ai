import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle

df = pd.read_csv('canada_per_capita_income.csv')

plt.xlabel('year')
plt.ylabel('per capita(US$)')
plt.scatter(df.year, df.per_capita, color='red', marker='+')

reg_model = linear_model.LinearRegression()
reg_model.fit(df[['year']].values, df.per_capita)

per_capita_2021 = reg_model.predict([[2021]])

print('per_capita_2021: ', per_capita_2021)

with open('saved_model', 'wb') as file:
    pickle.dump(reg_model, file)

with open('saved_model', 'rb') as file:
    model = pickle.load(file)

print('per capita 2050: ', model.predict([[2050]]))
