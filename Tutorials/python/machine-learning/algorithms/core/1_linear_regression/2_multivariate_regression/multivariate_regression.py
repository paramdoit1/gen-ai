import pandas as pd
from sklearn import linear_model
import joblib
import math

df = pd.read_csv('hiring.csv')

median_test_score = math.floor(df.test_score.median())
df.test_score = df.test_score.fillna(median_test_score)

mul_model = linear_model.LinearRegression()
mul_model.fit(df[['experience', 'test_score', 'interview_score']].values, df.salary)

salary_1 = mul_model.predict([[7, 9, 6]])
salary_2 = mul_model.predict([[12, 9, 8]])

print('salary_1', salary_1)
print('salary_2', salary_2)

joblib.dump(mul_model, 'saved_model')
model = joblib.load('saved_model')

salary_3 = mul_model.predict([[15, 9, 9]])

print('salary_3', salary_3)