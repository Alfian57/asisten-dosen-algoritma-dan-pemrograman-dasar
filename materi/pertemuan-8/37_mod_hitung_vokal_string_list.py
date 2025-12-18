# CHALLENGE MODIFIKASI
# Hitung juga huruf 'y' sebagai vokal (tambahkan 'y' ke list pengecekan).

# Hitung Vokal (String/List)
# Tujuan: Menghitung jumlah huruf vokal dalam kalimat

# MODIFIKASI: Tambahkan 'y' dan 'Y' ke list vokal
vokal = ['a', 'i', 'u', 'e', 'o', 'y', 'A', 'I', 'U', 'E', 'O', 'Y']
kalimat = input("Masukkan kalimat: ")

counter = 0
for huruf in kalimat:
    if huruf in vokal:
        counter += 1

print(f"Jumlah huruf vokal: {counter}")
