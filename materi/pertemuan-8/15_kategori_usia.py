# Kategori Usia
# Tujuan: Mengelompokkan usia manusia

usia = int(input("Masukkan usia: "))

if usia >= 0 and usia <= 5:
    kategori = "Balita"
elif usia >= 6 and usia <= 12:
    kategori = "Anak"
elif usia >= 13 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print(f"Kategori usia: {kategori}.")
