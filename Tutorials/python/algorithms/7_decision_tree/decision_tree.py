import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

df = pd.read_csv('salaries.csv')
print(df.head())

X = df.drop('salary_more_then_100k', axis='columns')
y = df['salary_more_then_100k']

le_company = LabelEncoder()
le_job = LabelEncoder()
le_degree = LabelEncoder()

X['company_n'] = le_company.fit_transform(X['company'])
X['job_n'] = le_job.fit_transform(X['job'])
X['degree_n'] = le_degree.fit_transform(X['degree'])

X_n = X.drop(['company','job', 'degree'], axis='columns')

model= tree.DecisionTreeClassifier()
model.fit(X_n.values, y)

score = model.score(X_n.values, y)
print('score: ', score)

predict_result = model.predict([[2,2,1]])
print('Predicted Result: ', predict_result)