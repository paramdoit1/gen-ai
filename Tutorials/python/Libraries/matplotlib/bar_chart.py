import pandas as pd
from matplotlib import pyplot as plt

df_sales =pd.read_excel('data/linechart.xlsx')
print(df_sales.head(5))

#df_sales.plot(kind="bar", x="Quarter")
#plt.xticks(rotation = 45)
#plt.show()

df_sales1=df_sales.set_index('Quarter')
#No need to set x if the x column is set as index
df_sales1.plot(kind="bar")
plt.xticks(rotation = 45)
plt.show()