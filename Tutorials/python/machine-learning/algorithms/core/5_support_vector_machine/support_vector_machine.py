import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

df['flower_names'] = df.target.apply(lambda x: iris.target_names[x])

df0 = df[:50]
df1 = df[50:100]
df2 = df[100:]

X = df.drop(['target', 'flower_names'], axis='columns')
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=10)

model= SVC()
model.fit(X_train.values, y_train)

accuracy = model.score(X_test.values, y_test)
print('accuracy: ', accuracy)

predicted_result = model.predict([[7.8, 7.8, 6.5, 1.3]])
print('predicted result', iris.target_names[predicted_result])
