# Tiket Kereta Api
# Tujuan: Menghitung harga tiket berdasarkan kelas dan jarak tujuan

kelas = input("Masukkan kelas (Ekonomi/Bisnis/Eksekutif): ")
tujuan = input("Masukkan tujuan (Bandung/Surabaya): ")
jumlah_tiket = int(input("Masukkan jumlah tiket: "))

# Tentukan harga dasar
if kelas == "Ekonomi":
    harga_dasar = 100000
elif kelas == "Bisnis":
    harga_dasar = 250000
elif kelas == "Eksekutif":
    harga_dasar = 500000
else:
    harga_dasar = 0

# Cek tujuan
biaya_ekstra = 0
if tujuan == "Surabaya":
    biaya_ekstra = 50000

# Hitung total
total = (harga_dasar + biaya_ekstra) * jumlah_tiket

print(f"Total harga tiket ke {tujuan}: Rp {total}")
