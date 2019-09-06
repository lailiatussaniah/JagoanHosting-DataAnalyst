import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print ('import data mtcars ke Python\n============================')
data = r'D:\Jagoan hosting\mtcars.xlsx'
df = pd.read_excel (data)
df.head()

print ('Buat Kolom Baru mpg_level\n=============================')
low = 'Low'
medium = 'Medium'
hard = 'Hard'
m = df['mpg'] < 20
m2= (df['mpg']>20) & (df['mpg']<30)
df['mpg_level']=np.where(m,low, np.where(m2,medium,hard))
print (df)

print ('Scatter Plot\n===============================')
area = np.pi*3
plt.figure(1)
plt.scatter(x=df['wt'], y=df['mpg'], s=area, alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('wt')
plt.ylabel('mpg')

print ('Bar Chart\n===============================')
objects = df['Cars']
y_pos = np.arange(len(objects))
performance = df['mpg']
plt.figure(2)
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xticks(rotation=90)
plt.ylabel('Milles Per Gallon')
plt.title('Barchart')
plt.show()

