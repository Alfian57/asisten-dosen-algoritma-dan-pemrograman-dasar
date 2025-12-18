# Cek Kata Sandi Lemah/Kuat
# Tujuan: Validasi panjang password

password = input("Masukkan password: ")

if len(password) < 8:
    print("Password Lemah")
else:
    print("Password Kuat")
