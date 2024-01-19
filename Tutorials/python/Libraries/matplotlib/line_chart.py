import pandas as pd
from matplotlib import pyplot as plt

df_sales =pd.read_excel('data/linechart.xlsx')
print(df_sales.head(5))

plt.plot(df_sales['Quarter'], df_sales['Fridge'], label = 'Fridge', color ="Green")
plt.plot(df_sales['Quarter'], df_sales['Dishwasher'], label = 'Dishwasher', color ="Blue")
plt.plot(df_sales['Quarter'], df_sales['Washing Machine'],  label = 'Washing Machine', color ="Orange")

plt.title("Product Sales")
plt.ylabel('Revenue(mln $)')
plt.xlabel('Financial Quarter')

plt.legend()
plt.show()