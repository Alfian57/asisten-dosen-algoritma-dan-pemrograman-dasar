# CHALLENGE MODIFIKASI
# Tambah grade D (Nilai 40-59).

# Konversi Nilai Huruf
# Tujuan: Mengubah nilai angka menjadi huruf mutu

nilai = int(input("Masukkan nilai angka (0-100): "))

if nilai >= 85 and nilai <= 100:
    huruf = "A"
elif nilai >= 70 and nilai <= 84:
    huruf = "B"
elif nilai >= 60 and nilai <= 69:
    huruf = "C"
# MODIFIKASI: Tambah grade D untuk nilai 40-59
elif nilai >= 40 and nilai <= 59:
    huruf = "D"
else:
    huruf = "E"

print(f"Nilai Anda: {huruf}.")
