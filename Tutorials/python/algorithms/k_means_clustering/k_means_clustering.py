import pandas as pd
from matplotlib import pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('E:\\mydocs\\git\\gen-ai\\Tutorials\\python\\algorithms\\k_means_clustering\\income.csv')
df = df.drop(['Name'], axis='columns')
'''
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df)
df['cluster'] = y_predicted
print(df.head())
print(km.cluster_centers_)

df0 =df[df.cluster == 0]
df1 = df[df.cluster == 1]
df2 = df[df.cluster == 2]

plt.scatter(df0.Age, df0['Income($)'], color = 'green')
plt.scatter(df1.Age, df1['Income($)'], color = 'red')
plt.scatter(df2.Age, df2['Income($)'], color = 'blue')

plt.scatter(km.cluster_centers_[:0], km.cluster_centers_[:, 1], color = 'purple', marker = "*")

plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

'''
scalar =MinMaxScaler()
scalar.fit(df[['Income($)']])
df['Income($)']  = scalar.transform(df[['Income($)']])

scalar.fit(df[['Age']])
df['Age'] = scalar.transform(df[['Age']])
print(df.head())

km = KMeans(n_clusters=3)
y_predicted = km.fit_predict(df)
df['cluster'] = y_predicted

df0 =df[df.cluster == 0]
df1 = df[df.cluster == 1]
df2 = df[df.cluster == 2]

plt.scatter(df0.Age, df0['Income($)'], color = 'green')
plt.scatter(df1.Age, df1['Income($)'], color = 'red')
plt.scatter(df2.Age, df2['Income($)'], color = 'blue')
plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:, 1], color = 'purple', marker = "*")

plt.xlabel('Age')
plt.ylabel('Income')
plt.show()
