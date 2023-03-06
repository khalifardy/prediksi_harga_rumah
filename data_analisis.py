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
from library import analisis_data_na
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
