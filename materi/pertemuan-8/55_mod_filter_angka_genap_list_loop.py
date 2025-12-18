# CHALLENGE MODIFIKASI
# Ganti filter-nya. Hanya masukkan angka yang lebih besar dari 3 ke list baru.

# Filter Angka Genap (List + Loop)
# Tujuan: Memisahkan angka genap dari list

angka_list = [1, 2, 3, 4, 5, 6]
# MODIFIKASI: Ganti jadi filter lebih besar dari 3
angka_lebih_besar_3 = []

print(f"List awal: {angka_list}")

for angka in angka_list:
    # MODIFIKASI: Filter yang lebih besar dari 3
    if angka > 3:
        angka_lebih_besar_3.append(angka)

print(f"List baru (> 3): {angka_lebih_besar_3}")
