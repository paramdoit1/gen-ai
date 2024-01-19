from cProfile import label
import pandas as pd
from matplotlib import pyplot as plt

df_sales =pd.read_excel('data/linechart.xlsx')
print(df_sales.head(5))

total_sales = df_sales[['Fridge', 'Dishwasher', 'Washing Machine']].sum()

print("Total Sales: \n",total_sales)

plt.pie(total_sales, labels=total_sales.index, autopct="%.2f%%", 
explode=(0.1, 0 ,0), shadow=True, startangle=120)

plt.show()