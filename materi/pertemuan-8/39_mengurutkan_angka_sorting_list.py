# Mengurutkan Angka (Sorting List)
# Tujuan: Mengurutkan input angka dari user

angka_list = []

print("Masukkan 5 angka acak:")
for i in range(5):
    angka = int(input(f"Angka ke-{i+1}: "))
    angka_list.append(angka)

print(f"List sebelum diurutkan: {angka_list}")

angka_list.sort()

print(f"List terurut: {angka_list}")
