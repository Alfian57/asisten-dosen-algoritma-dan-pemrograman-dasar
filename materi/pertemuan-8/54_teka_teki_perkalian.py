# Teka-Teki Perkalian
# Tujuan: User harus menjawab soal perkalian dengan benar agar program berhenti

soal_a = 7
soal_b = 8
jawaban_benar = soal_a * soal_b

print(f"Berapa hasil dari {soal_a} x {soal_b}?")

while True:
    jawaban = int(input("Jawaban Anda: "))
    
    if jawaban == jawaban_benar:
        print("Benar!")
        break
    else:
        print("Salah, coba lagi.")
