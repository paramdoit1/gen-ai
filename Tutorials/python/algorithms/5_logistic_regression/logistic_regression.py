import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('./insurance_data.csv')
print(df.head())

X = df[['age']]
y=df['bought_insurance']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=10)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

result = classifier.predict(X_test)
print(result)

accuracy = classifier.score(X_test, y_test)

print(accuracy)