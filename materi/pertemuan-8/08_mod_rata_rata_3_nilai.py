# CHALLENGE MODIFIKASI
# Hitung median dari 3 nilai (nilai tengah setelah diurutkan).

# Rata-rata 3 Nilai
# Tujuan: Menghitung nilai rata-rata dari 3 mata pelajaran

nilai_a = float(input("Masukkan nilai A: "))
nilai_b = float(input("Masukkan nilai B: "))
nilai_c = float(input("Masukkan nilai C: "))

rata_rata = (nilai_a + nilai_b + nilai_c) / 3

print(f"Nilai rata-rata kamu adalah {rata_rata:.2f}.")

# MODIFIKASI: Hitung median (nilai tengah setelah diurutkan)
nilai_list = [nilai_a, nilai_b, nilai_c]
nilai_list.sort()
median = nilai_list[1]
print(f"Nilai median kamu adalah {median}.")
