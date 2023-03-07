#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# %%source
"""
proses yang dilakukan :
1. Data yang hilang (NA)
2. Kolom-kolom angka (numerik)
3. Distribusi dari setiap kolom numerik
4. outlier
5. Kolom-kolom kategori dan jumlah kategorinya
6. Hubungan antara variabel independen dan dependen
"""
# %%
# open data
dataku = pd.read_csv('harga_rumah.csv')
#mendeteksi data-data kosong
kolom_na = [kolom for kolom in dataku.columns if dataku[kolom].isnull().sum() > 0]
var_na  = dataku[kolom_na]

# %%
# menghitung presentase var berisi NaN
var_na.isnull().mean() *100
# %%
# membuat visualisasi untuk semua variabel yang memiliki data kosong
from library import analisis_data_na,analisis_data_tahun,analisis_data_diskrit,analisis_data_kontinu, analisis_logtransform, analisis_logtransform2, analisis_outlier
batas = len(kolom_na)
i = 1

for kolom in kolom_na:
    i += 1
    analisis_data_na(dataku,kolom,"SalePrice")
    if i <= batas:plt.figure()
# %%
#Menganalisis kolom-kolom numerik
#dtypes 'O' adalah string

kolom_numerik = [kolom for kolom in dataku.columns if dataku[kolom].dtypes != 'O']
data_numerik = dataku[kolom_numerik]
# %%

"""
Variabel yang berhubungan dengan waktu:
    1. YearBuilt = kapan rumah dibangun
    2. YearRemodAdd = kapan rumah di renov
    3. GarageYrBlt = kapan garasinya dibangun
    4. YrSold = kapan rumahnya di jual
"""

# %%
kolom_tahun = [
    kolom for kolom in kolom_numerik if "Year" in kolom or "Yr" in kolom
]
# %%
tahun = dataku[kolom_tahun]
# %%
#visualisasi antara tahun penjualan dengan SalePrice
dataku.groupby("YrSold")["SalePrice"].median().plot()
plt.ylabel("Nilai Median Harga Jual Rumah")
plt.xlabel("Perubahan Harga Per Tahun")
plt.tight_layout()
# %%

batas = len(kolom_tahun)
i = 1
for kolom in kolom_tahun:
    if kolom != 'YrSold':
        i += 1
        analisis_data_tahun(dataku,kolom,"YrSold","SalePrice","Harga Jual Rumah")
        if i < batas: plt.figure()
    
#
# %%
#Menganalisa data diskrit
kolom_diskrit = [
    kolom for kolom in kolom_numerik if len(dataku[kolom].unique())<=15 and kolom not in kolom_tahun +['id']
]
diskrit = dataku[kolom_diskrit]

# %%
#visualisasi antara data diskrit dengan SalePrice
batas = len(kolom_diskrit)
i = 1
for kolom in kolom_diskrit:
    i += 1
    analisis_data_diskrit(dataku,kolom,"SalePrice","Median Harga Jual")
    if i < batas: plt.figure()

# %%
#variabel kontinu
kolom_kontinu = [
    kolom for kolom in kolom_numerik if kolom not in kolom_diskrit and kolom not in kolom_tahun +['id']
]
kontinu = dataku[kolom_kontinu]
# %%
for i in kontinu:
    print(len(dataku[i].unique()))
# %%
batas = len(kolom_kontinu)
i = 1

for kolom in kolom_kontinu:
    i +=1
    analisis_data_kontinu(dataku,kolom,"Jumlah rumah")
    if i <= batas: plt.figure()
# %%
#melakukan proses log transform (karena data tidak terdistribusi normal maka dilakuka n log transform)

batas = 0
kolom_kontinu_log = []

for kolom in kolom_kontinu:
    if any(dataku[kolom]) <= 0:
        pass
    else:
        kolom_kontinu_log.append(kolom)
        i += 1

kontinu_log = dataku[kolom_kontinu_log]

# %%
i = 1
for kolom in kolom_kontinu_log:
    i += 1
    analisis_logtransform(dataku,kolom,"Jumlah rumah")
    if i <= batas: plt.figure()

# %%
i = 1
for kolom in kolom_kontinu_log:
    if kolom != 'SalePrice':
        i += 1
        analisis_logtransform2(dataku,kolom,"SalePrice","Harga Rumah")
        if i <= batas: plt.figure()

# %%
#analisis outlier
i = 1
for kolom in kolom_kontinu_log:
    i += 1
    analisis_outlier(dataku,kolom)
    if i <= batas: plt.figure()
# %%
