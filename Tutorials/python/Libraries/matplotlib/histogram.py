import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df_score =pd.read_excel('data/histograms.xlsx')
print(df_score.head(5)) 

#Using matplotlib to draw histogram
#plt.hist(df_score['Exam_Score'])
#plt.show()

#Using seabprn to draw histogram
#added Kernel density estimation
#sns.histplot(df_score['Exam_Score'], kde=True)

sns.histplot(data = df_score, x='Exam_Score', kde=True)

plt.xlabel("Score")
plt.ylabel('Count')
plt.title('Exam Scores')
plt.show()

