import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("--- 1. Data Gaji Karyawan ---")
df = pd.read_csv('/home/alfiang/Asdos/algoritma-dan-pemrograman-dasar/materi/pertemuan-12/challenge/data_karyawan.csv')

print("--- Data Awal ---")
print(df)
print("\n")

df['Gaji_Bersih'] = df['Gaji_Pokok'] + df['Tunjangan']

print("--- 2. Data Setelah Hitung Gaji Bersih ---")
print(df[['Nama', 'Gaji_Bersih']])
print("\n")

# Analisis Sederhana (NumPy/Pandas Basic)
rata_gaji = df['Gaji_Bersih'].mean()
print(f"Rata-rata Gaji di Perusahaan: Rp {rata_gaji}")


print("\n--- 3. Membuat Grafik Gaji ---")

plt.plot(df['Nama'], df['Gaji_Bersih'], color='teal')

# Hiasan (Optional tapi diajarkan di slide Matplotlib dasar)
plt.title('Laporan Gaji Bersih Karyawan')
plt.xlabel('Nama Karyawan')
plt.ylabel('Total Pendapatan (Rupiah)')

plt.show()