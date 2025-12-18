# CHALLENGE MODIFIKASI
# Hapus syarat 'Performa'. Jadi bonus hanya berdasarkan Lama Bekerja saja.

# Bonus Karyawan
# Tujuan: Menghitung bonus akhir tahun dengan kondisi bertingkat

lama_bekerja = int(input("Masukkan lama bekerja (tahun): "))
gaji = int(input("Masukkan gaji pokok: "))

bonus = 0

# MODIFIKASI: Hapus syarat performa, hanya berdasarkan lama bekerja
if lama_bekerja > 5:
    bonus = 5 * gaji
elif lama_bekerja >= 2:
    bonus = 1 * gaji
else:
    bonus = 0

print(f"Bonus yang diterima: Rp {bonus}")
