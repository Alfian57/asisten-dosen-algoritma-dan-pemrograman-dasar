# Program Hitung Umur
# Tujuan: Menghitung tahun kelahiran berdasarkan umur saat ini

nama = input("Masukkan nama Anda: ")
umur = int(input("Masukkan umur Anda: "))

tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur

print(f"Halo {nama}, kamu lahir pada tahun {tahun_lahir}.")
