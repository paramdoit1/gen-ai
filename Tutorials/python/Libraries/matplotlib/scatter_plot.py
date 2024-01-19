import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_excel("data/scatter_plot.xlsx")
print(df)

sns.scatterplot(data=df, x='area_square_ft' , y="price")
plt.xlabel("Area Square Feet")
plt.ylabel('Price')
plt.title('Price Square Feet')
plt.show()