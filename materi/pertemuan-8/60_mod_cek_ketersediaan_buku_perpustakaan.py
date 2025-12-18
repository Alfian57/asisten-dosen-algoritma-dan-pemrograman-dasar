# CHALLENGE MODIFIKASI
# Tambahkan kondisi default: Jika buku tidak ada di dictionary, print 'Buku tidak dijual'.

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
    # MODIFIKASI: Ubah pesan jadi 'Buku tidak dijual'
    print("Buku tidak dijual")
