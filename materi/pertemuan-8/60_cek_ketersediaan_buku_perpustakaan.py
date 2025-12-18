# Cek Ketersediaan Buku (Perpustakaan)
# Tujuan: Mengecek status buku

perpustakaan = {
    'Harry Potter': 'Tersedia',
    'Laskar Pelangi': 'Dipinjam',
    'Bumi Manusia': 'Tersedia',
    'Ronggeng Dukuh Paruk': 'Dipinjam'
}

judul_buku = input("Masukkan judul buku: ")

if judul_buku in perpustakaan:
    print(f"Buku '{judul_buku}' statusnya: {perpustakaan[judul_buku]}")
else:
    print("Buku tidak ditemukan")
