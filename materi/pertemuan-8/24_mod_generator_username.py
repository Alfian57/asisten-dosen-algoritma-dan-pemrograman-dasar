# CHALLENGE MODIFIKASI
# Ubah format usernamenya. Jadi: TahunLahir + NamaDepan (Dibalik).

# Generator Username
# Tujuan: Membuat username otomatis

def create_username(nama_depan, tahun_lahir):
    # MODIFIKASI: Format jadi TahunLahir + NamaDepan (dibalik)
    nama_dibalik = nama_depan[::-1]
    username = str(tahun_lahir) + nama_dibalik
    return username

nama_depan = input("Masukkan nama depan: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))

username = create_username(nama_depan, tahun_lahir)

print(f"Username Anda: {username}")
