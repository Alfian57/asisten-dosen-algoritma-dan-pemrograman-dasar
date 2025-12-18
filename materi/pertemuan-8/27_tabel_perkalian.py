# Tabel Perkalian
# Tujuan: Menampilkan tabel perkalian untuk angka tertentu

angka = int(input("Masukkan angka perkalian: "))

print(f"Tabel perkalian {angka}:")
for i in range(1, 11):
    hasil = i * angka
    print(f"{i} x {angka} = {hasil}")
