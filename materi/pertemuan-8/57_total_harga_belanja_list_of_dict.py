# Total Harga Belanja (List of Dict)
# Tujuan: Menghitung total keranjang belanja

keranjang = [
    {'nama': 'Roti', 'harga': 5000},
    {'nama': 'Susu', 'harga': 10000},
    {'nama': 'Telur', 'harga': 15000}
]

total_belanja = 0

for barang in keranjang:
    total_belanja += barang['harga']

print(f"Total Belanja: Rp {total_belanja}")
