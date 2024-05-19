import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('./carprices.csv')
print(df.head())

X = df[['Mileage', 'Age(yrs)']]
y=df['Sell Price($)']
#plt.scatter(df['Mileage'],df['Sell Price($)'])
#plt.show()

#plt.scatter(df['Age(yrs)'], df['Sell Price($)'])
#plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=10)

classifier = LinearRegression()
classifier.fit(X_train, y_train)

result = classifier.predict(X_test)
print(result)

accuracy = classifier.score(X_test, y_test)

print(accuracy)