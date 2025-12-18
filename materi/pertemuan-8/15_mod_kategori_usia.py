# CHALLENGE MODIFIKASI
# Tambah kategori "Balita" (usia < 5).
# CATATAN: File asli sudah ada kategori Balita, jadi challenge ini sepertinya typo.
# Jika ada kategori Balita di asli 0-5, maka kita bisa ubah jadi 0-4 untuk balita, 5-12 anak

# Kategori Usia
# Tujuan: Mengelompokkan usia manusia

usia = int(input("Masukkan usia: "))

# MODIFIKASI: Sudah ada Balita, kita pastikan Balita untuk usia < 5
if usia >= 0 and usia < 5:
    kategori = "Balita"
elif usia >= 5 and usia <= 12:
    kategori = "Anak"
elif usia >= 13 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print(f"Kategori usia: {kategori}.")
