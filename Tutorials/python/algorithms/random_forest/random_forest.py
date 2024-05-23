from unicodedata import digit
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix

digits = load_digits()
df = pd.DataFrame(digits.data)

X_train, X_test, y_train, y_test = train_test_split(df, digits.target, test_size=0.2, random_state=10)

model = RandomForestClassifier(n_estimators=50)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(score)

y_predicted = model.predict(X_test)

cm = confusion_matrix(y_test, y_predicted)
print('Confusion Matrix: ', cm)

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()

