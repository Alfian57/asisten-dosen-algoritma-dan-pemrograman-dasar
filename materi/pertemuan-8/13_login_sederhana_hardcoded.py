# Login Sederhana (Hardcoded)
# Tujuan: Validasi username dan password

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "admin" and password == "12345":
    print("Login Sukses")
else:
    print("Login Gagal")
