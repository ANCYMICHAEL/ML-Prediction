import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df = df.pivot(index='Video_Title', columns='Quarters', values='Revenue')
df.plot(kind='bar', figsize=(15, 8), color=['red', 'blue', '#e37827', '#275444'])

plt.xlabel('Video Title')
plt.ylabel('Revenue')
plt.title('Chart Title')
plt.show()
