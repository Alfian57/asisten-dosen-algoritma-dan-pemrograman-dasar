import pandas as pd

df = pd.read_csv("data_transaksi.csv")
# print(df)

harga_tinggi = df[df["Harga"] > 100000]
jumlah_terbatas = harga_tinggi[harga_tinggi["Jumlah"] < 5]
print(jumlah_terbatas)

# Ambil 5 baris pertama
# print(df.head())

# Ambil 5 baris terakhir
# print(df.tail())

# print(df.shape)
# print(df.info())

# Statistik
# print(df.describe())