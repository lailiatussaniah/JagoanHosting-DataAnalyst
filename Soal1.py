import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from matplotlib import rc

print ('============================\nimport data inflasi ke Python\n============================')
data = r'D:\Jagoan hosting\inflasi.xlsx'
df = pd.read_excel (data)
df.head()
print(df)

print ('=======================================\nAnalisis Deskirptif inflasi Semua Data Inflasi\n=======================================')
Data_inflasi = df['Inflasi']
print(Data_inflasi)
JumlahData = len(Data_inflasi)
Mean = Data_inflasi.mean()
Median = Data_inflasi.median()
Modus = Data_inflasi.mode()
Min = min(Data_inflasi)
Max = max(Data_inflasi)
StandarDeviasi = statistics.stdev(Data_inflasi)

print('Jumlah Data = ', JumlahData)
print('Mean = ', Mean)
print('Median = ', Median)
print ('Modus = ')
print(Modus)
print('Nilai Standar Deviasi = ', StandarDeviasi)
print('Nilai Inflasi Terkecil =', Min)
print('Nilai Inflasi Terbesar =', Max)

print ('================================\nAnalisis Deskirptif tiap tahun (2002-2019)\n================================')
inflasi2019 = df.iloc[0:6,[1]]
inflasi2018 = df.iloc[6:18,[1]]
inflasi2017 = df.iloc[18:30,[1]]
inflasi2016 = df.iloc[30:42,[1]]
inflasi2015 = df.iloc[42:54,[1]]
inflasi2014 = df.iloc[54:66,[1]]
inflasi2013 = df.iloc[66:78,[1]]
inflasi2012 = df.iloc[78:90,[1]]
inflasi2011 = df.iloc[90:102,[1]]
inflasi2010 = df.iloc[102:114,[1]]
inflasi2009 = df.iloc[114:126,[1]]
inflasi2008 = df.iloc[126:138,[1]]
inflasi2007 = df.iloc[138:150,[1]]
inflasi2006 = df.iloc[150:162,[1]]
inflasi2005 = df.iloc[162:174,[1]]
inflasi2004 = df.iloc[174:186,[1]]
inflasi2003 = df.iloc[186:198,[1]]
inflasi2002 = df.iloc[198,[1]]

Listinflasi = [inflasi2019, inflasi2018,inflasi2017, inflasi2016, inflasi2015, inflasi2014,
                inflasi2013, inflasi2012,inflasi2011,inflasi2010, inflasi2009, inflasi2008,
                inflasi2007, inflasi2006, inflasi2005, inflasi2004, inflasi2003, inflasi2002 ]
ListMean =[]
ListMin =[]
ListMax =[]
for i in Listinflasi:

    JumlahDataInflasiPerTahun = len(i)
    MeanData = i.mean()
    MedianData = i.median()
    MinData = i.min()
    MaxData = i.max()
    StandarDeviasiData = i.std()
    ListMean.append(MeanData)
    ListMin.append(MinData)
    ListMax.append(MaxData)
    print(i)
    print('Jumlah Data = ',JumlahDataInflasiPerTahun )
    print('Mean = ',MeanData )
    print('Median = ', MedianData )
    print('Min = ', MinData )
    print('Max = ', MaxData)
    print('Standar Deviasi = ', StandarDeviasiData)
    print ('===============================')
    
print ('================================\n Grafik Rata-rata inflasi tiap tahun \n================================')
Tahun = ['2019','2018','2017','2016', '2015', '2014','2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002']
plt.figure(1)
plt.rcParams["figure.figsize"] = (8, 8)
plt.plot(Tahun,ListMean, 'c-o')
plt.xticks(rotation=90)
plt.title('Grafik Rata - rata inflasi tiap tahun (2002-2019)')
plt.xlabel('Tahun') #keterangan sumbu x
plt.ylabel('inflasi') #keterangan sumbu y

print ('================================\n Grafik inflasi terkecil (MIN) tiap tahun \n================================')
plt.figure(2)
plt.rcParams["figure.figsize"] = (8, 8)
plt.bar(Tahun,ListMin, color = "yellow")
plt.xticks(rotation=90)
plt.title('Grafik inflasi terkecil tiap tahun (2002-2019)')
plt.xlabel('Tahun') #keterangan sumbu x
plt.ylabel('inflasi') #keterangan sumbu y
plt.show()
