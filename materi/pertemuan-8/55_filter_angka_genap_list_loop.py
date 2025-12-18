# Filter Angka Genap (List + Loop)
# Tujuan: Memisahkan angka genap dari list

angka_list = [1, 2, 3, 4, 5, 6]
angka_genap = []

print(f"List awal: {angka_list}")

for angka in angka_list:
    if angka % 2 == 0:
        angka_genap.append(angka)

print(f"List baru (genap saja): {angka_genap}")
