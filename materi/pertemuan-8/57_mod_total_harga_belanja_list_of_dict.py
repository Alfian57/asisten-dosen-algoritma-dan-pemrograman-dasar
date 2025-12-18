# CHALLENGE MODIFIKASI
# Tambahkan pajak 10% pada total akhir belanja.

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

# MODIFIKASI: Tambahkan pajak 10%
pajak = total_belanja * 0.1
total_dengan_pajak = total_belanja + pajak

print(f"Total Belanja: Rp {total_belanja}")
print(f"Pajak 10%: Rp {int(pajak)}")
print(f"Total dengan Pajak: Rp {int(total_dengan_pajak)}")
