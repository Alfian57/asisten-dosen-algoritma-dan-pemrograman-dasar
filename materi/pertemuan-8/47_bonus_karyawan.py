# Bonus Karyawan
# Tujuan: Menghitung bonus akhir tahun dengan kondisi bertingkat

lama_bekerja = int(input("Masukkan lama bekerja (tahun): "))
performa = input("Masukkan performa (Sangat Baik/Baik/Cukup): ")
gaji = int(input("Masukkan gaji pokok: "))

bonus = 0

if lama_bekerja > 5 and performa == "Sangat Baik":
    bonus = 5 * gaji
elif lama_bekerja > 5 and performa == "Baik":
    bonus = 3 * gaji
elif lama_bekerja >= 2:
    bonus = 1 * gaji
else:
    bonus = 0

print(f"Bonus yang diterima: Rp {bonus}")
