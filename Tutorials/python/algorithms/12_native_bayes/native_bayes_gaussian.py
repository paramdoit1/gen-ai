# Getting if titanic passanger survived or not

import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('titanic.csv')
print(df.columns)

input = df[['Pclass', 'Sex', 'Age', 'Fare', 'Survived']]
target =df['Survived']

input.Sex = input.Sex.apply(lambda x: 1 if(x=='male') else 0)
print(input.columns[input.isna().any()])
input.Age = input.Age.fillna(input.Age.mean())

X_train, X_test, y_train, y_test = train_test_split(input, target, test_size=0.2)
model = GaussianNB()

model.fit(X_train, y_train)  
score = model.score(X_test, y_test)
print(score)

predict_result = model.predict(X_test[0:10])
print('predict_result', predict_result)

cross_val_score = cross_val_score(GaussianNB(), X_train, y_train, cv=5)
print('cross_val_score: ', cross_val_score)




