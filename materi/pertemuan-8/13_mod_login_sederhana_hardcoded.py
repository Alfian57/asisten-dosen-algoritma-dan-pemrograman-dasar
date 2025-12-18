# CHALLENGE MODIFIKASI
# Ubah username dan password hardcode-nya jadi nilai yang berbeda.

# Login Sederhana (Hardcoded)
# Tujuan: Validasi username dan password

username = input("Masukkan username: ")
password = input("Masukkan password: ")

# MODIFIKASI: Ubah username dan password
if username == "student" and password == "abcd1234":
    print("Login Sukses")
else:
    print("Login Gagal")
