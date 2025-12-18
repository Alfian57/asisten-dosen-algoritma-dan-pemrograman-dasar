# CHALLENGE MODIFIKASI
# Hapus penjelasan (print rumus tahun kabisat). Jadi hanya output "Kabisat" atau "Bukan".

# Cek Tahun Kabisat
# Tujuan: Menentukan apakah suatu tahun adalah kabisat

tahun = int(input("Masukkan tahun: "))

# MODIFIKASI: Output lebih sederhana, hanya "Kabisat" atau "Bukan Kabisat"
if (tahun % 4 == 0) and (tahun % 100 != 0 or tahun % 400 == 0):
    print("Kabisat")
else:
    print("Bukan Kabisat")
