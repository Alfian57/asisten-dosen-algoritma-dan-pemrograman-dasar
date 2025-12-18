# CHALLENGE MODIFIKASI
# Hapus fitur diskon. Jadi program hanya kasir beli buku sederhana.

# Kasir Toko Buku (Diskon Tetap)
# Tujuan: Menghitung total harga pembelian buku

harga_buku = int(input("Masukkan harga buku: "))
jumlah_buku = int(input("Masukkan jumlah buku: "))

# MODIFIKASI: Hapus diskon, hanya hitung total
total = harga_buku * jumlah_buku

print(f"Total bayar: Rp {int(total)}.")
