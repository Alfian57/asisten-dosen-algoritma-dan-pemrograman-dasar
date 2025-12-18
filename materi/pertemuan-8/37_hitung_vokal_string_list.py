# Hitung Vokal (String/List)
# Tujuan: Menghitung jumlah huruf vokal dalam kalimat

vokal = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
kalimat = input("Masukkan kalimat: ")

counter = 0
for huruf in kalimat:
    if huruf in vokal:
        counter += 1

print(f"Jumlah huruf vokal: {counter}")
