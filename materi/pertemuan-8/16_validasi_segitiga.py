# Validasi Segitiga
# Tujuan: Mengecek apakah 3 sisi bisa membentuk segitiga

sisi_a = float(input("Masukkan sisi A: "))
sisi_b = float(input("Masukkan sisi B: "))
sisi_c = float(input("Masukkan sisi C: "))

if (sisi_a + sisi_b > sisi_c) and (sisi_a + sisi_c > sisi_b) and (sisi_b + sisi_c > sisi_a):
    print("Bisa membentuk segitiga")
else:
    print("Tidak bisa membentuk segitiga")
