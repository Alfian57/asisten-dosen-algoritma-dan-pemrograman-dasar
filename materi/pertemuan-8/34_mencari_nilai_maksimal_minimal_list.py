# Mencari Nilai Maksimal & Minimal (List)
# Tujuan: Mencari nilai tertinggi dan terendah dari sekumpulan nilai

nilai_list = []

print("Masukkan 5 angka:")
for i in range(5):
    angka = int(input(f"Angka ke-{i+1}: "))
    nilai_list.append(angka)

# Cari nilai maksimal dan minimal tanpa max()/min()
nilai_max = nilai_list[0]
nilai_min = nilai_list[0]

for nilai in nilai_list:
    if nilai > nilai_max:
        nilai_max = nilai
    if nilai < nilai_min:
        nilai_min = nilai

print(f"Nilai Tertinggi: {nilai_max}, Terendah: {nilai_min}")
