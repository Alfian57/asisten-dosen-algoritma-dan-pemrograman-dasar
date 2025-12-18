# CHALLENGE MODIFIKASI
# Urutkan angkanya secara Terbalik (Descending/besar ke kecil).

# Mengurutkan Angka (Sorting List)
# Tujuan: Mengurutkan input angka dari user

angka_list = []

print("Masukkan 5 angka acak:")
for i in range(5):
    angka = int(input(f"Angka ke-{i+1}: "))
    angka_list.append(angka)

print(f"List sebelum diurutkan: {angka_list}")

# MODIFIKASI: Urutkan secara descending (terbalik)
angka_list.sort(reverse=True)

print(f"List terurut (Descending): {angka_list}")
