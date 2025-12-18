# CHALLENGE MODIFIKASI
# Ganti soalnya jadi penjumlahan: 10 + 20. Kunci jawabannya ganti jadi 30.

# Teka-Teki Perkalian
# Tujuan: User harus menjawab soal perkalian dengan benar agar program berhenti

# MODIFIKASI: Ganti jadi penjumlahan
soal_a = 10
soal_b = 20
jawaban_benar = 30  # 10 + 20

print(f"Berapa hasil dari {soal_a} + {soal_b}?")

while True:
    jawaban = int(input("Jawaban Anda: "))
    
    if jawaban == jawaban_benar:
        print("Benar!")
        break
    else:
        print("Salah, coba lagi.")
