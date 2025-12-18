# CHALLENGE MODIFIKASI
# Syaratnya diperketat. Panjang password harus lebih dari 10 karakter.

# Cek Kata Sandi Lemah/Kuat
# Tujuan: Validasi panjang password

password = input("Masukkan password: ")

# MODIFIKASI: Ubah batas jadi lebih dari 10 karakter
if len(password) > 10:
    print("Password Kuat")
else:
    print("Password Lemah")
