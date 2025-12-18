# CHALLENGE MODIFIKASI
# Ganti jadi tabel perkalian 1 sampai 5 saja. Jangan sampai 10.

# Tabel Perkalian
# Tujuan: Menampilkan tabel perkalian untuk angka tertentu

angka = int(input("Masukkan angka perkalian: "))

print(f"Tabel perkalian {angka}:")
# MODIFIKASI: Ubah range jadi 1 sampai 5
for i in range(1, 6):
    hasil = i * angka
    print(f"{i} x {angka} = {hasil}")
