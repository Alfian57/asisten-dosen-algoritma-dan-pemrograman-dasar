# Kalkulator Parkir Progresif
# Tujuan: Menghitung tarif dengan aturan bertingkat dan batas maksimal (Max Cap)

lama_parkir = int(input("Masukkan lama parkir (jam): "))

# Hitung biaya
if lama_parkir <= 0:
    total = 0
elif lama_parkir == 1:
    total = 3000
else:
    # 1 jam pertama = 3000, jam berikutnya 1000/jam
    total = 3000 + ((lama_parkir - 1) * 1000)

# Cek batas maksimal
if total > 10000:
    total = 10000

print(f"Biaya Parkir: Rp {total}")
