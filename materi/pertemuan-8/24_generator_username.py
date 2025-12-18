# Generator Username
# Tujuan: Membuat username otomatis

def create_username(nama_depan, nama_belakang, tahun_lahir):
    # Gabungkan nama depan + nama belakang + 2 digit terakhir tahun
    tahun_terakhir = str(tahun_lahir)[-2:]
    username = nama_depan + nama_belakang + tahun_terakhir
    return username

nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))

username = create_username(nama_depan, nama_belakang, tahun_lahir)

print(f"Username Anda: {username}")
