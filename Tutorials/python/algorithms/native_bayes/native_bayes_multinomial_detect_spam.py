# Detecting given mail is spam or not

import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.pipeline import Pipeline

df = pd.read_csv('spam.csv')
print(df.columns)

# Getting count of records group by spam or not
result = df.groupby('Category').describe()
print('result: ',result)

target = df.Category.apply(lambda x: 1 if(x=='spam')else 0)
X_train, X_test, y_train, y_test = train_test_split(df.Message, target, test_size=0.2)
vectorizer = CountVectorizer()
X_train_count = vectorizer.fit_transform(X_train.values)

model = MultinomialNB()
model.fit(X_train_count, y_train)

emails = [
    'Hey Mohan, can we get together to watch football match tomorrow?',
    'Upto 20 percent discount on parking,exclusive offer just for you. Dont miss this reward!'
]

emails_count = vectorizer.transform(emails)
predicted_count = model.predict(emails_count)
print('predicted_count : ', predicted_count)

X_test_count = vectorizer.transform(X_test)
score = model.score(X_test_count, y_test)
print('score: ', score)

#using Pipeline

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

classifier.fit(X_train, y_train)

score = classifier.score(X_test, y_test)
predicted_result = classifier.predict(emails)
print('predicted_result: ', predicted_result)
