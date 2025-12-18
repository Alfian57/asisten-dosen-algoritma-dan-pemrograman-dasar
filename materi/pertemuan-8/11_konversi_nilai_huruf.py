# Konversi Nilai Huruf
# Tujuan: Mengubah nilai angka menjadi huruf mutu

nilai = int(input("Masukkan nilai angka (0-100): "))

if nilai >= 85 and nilai <= 100:
    huruf = "A"
elif nilai >= 70 and nilai <= 84:
    huruf = "B"
elif nilai >= 60 and nilai <= 69:
    huruf = "C"
else:
    huruf = "D"

print(f"Nilai Anda: {huruf}.")
