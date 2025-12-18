# Kasir Toko Buku (Diskon Tetap)
# Tujuan: Menghitung total harga pembelian buku

harga_buku = int(input("Masukkan harga buku: "))
jumlah_buku = int(input("Masukkan jumlah buku: "))

total = harga_buku * jumlah_buku
diskon = 0.05 * total  # Diskon 5%
bayar = total - diskon

print(f"Total bayar setelah diskon 5%: Rp {int(bayar)}.")
