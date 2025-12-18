# CHALLENGE MODIFIKASI
# Ganti domain sekolahnya jadi @gmail.com.

# Generator Email Sekolah
# Tujuan: Membuat email dari Nama dan NIM

nama_depan = input("Masukkan nama depan: ")
nim = input("Masukkan NIM: ")

# Gabungkan dan lowercase
# MODIFIKASI: Ganti domain jadi @gmail.com
email = f"{nama_depan.lower()}.{nim}@gmail.com"

print(f"Email Anda: {email}")
