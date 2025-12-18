# CHALLENGE MODIFIKASI
# Hapus pencarian nilai Minimum. Hanya cari nilai Maksimal saja.

# Mencari Nilai Maksimal & Minimal (List)
# Tujuan: Mencari nilai tertinggi dan terendah dari sekumpulan nilai

nilai_list = []

print("Masukkan 5 angka:")
for i in range(5):
    angka = int(input(f"Angka ke-{i+1}: "))
    nilai_list.append(angka)

# MODIFIKASI: Hanya cari nilai maksimal
nilai_max = nilai_list[0]

for nilai in nilai_list:
    if nilai > nilai_max:
        nilai_max = nilai

print(f"Nilai Tertinggi: {nilai_max}")
