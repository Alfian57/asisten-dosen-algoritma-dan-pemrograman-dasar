# CHALLENGE MODIFIKASI
# Ubah outputnya pakai format f-string yang lebih panjang: 
# "Nama: {nama}, Tahun Lahir: {tahun_lahir}, Umur: {umur} tahun"

# Program Hitung Umur
# Tujuan: Menghitung tahun kelahiran berdasarkan umur saat ini

nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur

# MODIFIKASI: Output dengan format f-string yang lebih panjang
print(f"Nama: {nama}, Tahun Lahir: {tahun_lahir}, Umur: {umur} tahun")
