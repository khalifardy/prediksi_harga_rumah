import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

def analisis_data_na(data,col, var_dependen):
    data = data.copy()
    #mengecek setiap variabel jika ada Nan maka 1 , jika tidak maka 0
    data[col] = np.where(data[col].isnull(),1,0)
    #sekarang kita memiliki databinary 0 dan 1
    #selanjutnya adalah mengelompokan terhadap SalePrice(var dependen)
    data.groupby(col)[var_dependen].median().plot.bar()
    
    plt.title(col)
    plt.tight_layout()
    plt.show()
