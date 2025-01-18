from string import digits
from unicodedata import digit
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix

import seaborn as sn

digits = load_digits()
plt.gray()

X = digits.data
y= digits.target

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=10)

classifier = LogisticRegression(solver='lbfgs', max_iter=3000)
classifier.fit(X_train, y_train)

classifier.predict(X_test)
accuracy = classifier.score(X_test, y_test)

print(accuracy)

#plt.matshow(digits.images[67])

predicted_result1 = classifier.predict([digits.data[67]])
print('predicted_result1: ', predicted_result1)

predicted_result2 = classifier.predict(digits.data[0:5])
print('predicted_result2: ', predicted_result2)

y_predicted = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_predicted)
print('Confusion Matrix: ', cm)

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()