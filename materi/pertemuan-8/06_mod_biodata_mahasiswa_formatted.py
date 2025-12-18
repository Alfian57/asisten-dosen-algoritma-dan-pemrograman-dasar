# CHALLENGE MODIFIKASI
# Tambah field NPM (input string).

# Biodata Mahasiswa Formatted
# Tujuan: Menampilkan biodata dengan format rapi menggunakan f-string

nama = input("Masukkan nama: ")
nim = input("Masukkan NIM: ")
# MODIFIKASI: Tambah field NPM
npm = input("Masukkan NPM: ")
jurusan = input("Masukkan jurusan: ")
angkatan = input("Masukkan angkatan: ")

print(f"Mahasiswa bernama {nama} ({nim}) NPM {npm} dari jurusan {jurusan} angkatan {angkatan}.")
