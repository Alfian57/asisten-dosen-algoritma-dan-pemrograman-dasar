# Generator Email Sekolah
# Tujuan: Membuat email dari Nama dan NIM

nama_depan = input("Masukkan nama depan: ")
nim = input("Masukkan NIM: ")

# Gabungkan dan lowercase
email = f"{nama_depan.lower()}.{nim}@sekolah.ac.id"

print(f"Email Anda: {email}")
