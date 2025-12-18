import wikipedia
import qrcode
from tabulate import tabulate
from colorama import Fore, Style, init
import sys

# Setup
init(autoreset=True)
wikipedia.set_lang("id")

# Data Menu
menu_cafe = [
    ["1", "Espresso", 20000],
    ["2", "Cappuccino", 30000],
    ["3", "Green Tea Latte", 25000],
    ["4", "Americano", 22000],
    ["5", "Chocolate Ice", 28000]
]

# Header Aplikasi
print(Fore.CYAN + Style.BRIGHT + "=" * 50)
print(Fore.YELLOW + Style.BRIGHT + "SELAMAT DATANG DI SMART COFFEE CLI")
print(Fore.CYAN + Style.BRIGHT + "=" * 50)
print()

# Menampilkan Menu
print(Fore.WHITE + tabulate(menu_cafe, headers=["No", "Menu", "Harga"], tablefmt="fancy_grid"))
print()

# 3. Input Pesanan
try:
    nama_pembeli = input(Fore.GREEN + Style.RESET_ALL + "Masukkan Nama Anda: ")
    nomor_menu = input(Fore.GREEN + Style.RESET_ALL + "Pilih Nomor Menu (1-5): ")
    jumlah = int(input(Fore.GREEN + Style.RESET_ALL + "Jumlah Pesanan: "))
except ValueError:
    print(Fore.RED + "\nInput jumlah harus angka! Program berhenti.")
    sys.exit()

# Cari menu berdasarkan input nomor
item_dipilih = None
for item in menu_cafe:
    if item[0] == nomor_menu:
        item_dipilih = item
        break

nama_menu = item_dipilih[1]
harga_satuan = item_dipilih[2]
total_harga = harga_satuan * jumlah

print(Fore.YELLOW + "\n[...] Menghitung total...")

# 4. Fitur Edukasi (Wikipedia)
fakta_unik = wikipedia.summary(nama_menu, sentences=2)

# Tampilkan Fakta
print(Fore.CYAN + "\n" + "-" * 60)
print(Fore.WHITE + Style.BRIGHT + "TAHUKAH KAMU?")
print(Style.DIM + fakta_unik)
print(Fore.CYAN + "-" * 60)

# Tampilkan Total
print(Fore.GREEN + Style.BRIGHT + f"\nTOTAL BAYAR: {total_harga}")

# 5. Generasi QR Code
print(Fore.YELLOW + "Membuat QR Code Pembayaran...")

data_qr = f"BAYAR_{nama_pembeli.upper()}_{total_harga}"
nama_file_qr = f"Struk_{nama_pembeli.replace(' ', '_')}.png"

img = qrcode.make(data_qr)
img.save(nama_file_qr)

print(Fore.GREEN + Style.BRIGHT + f"Silakan scan '{nama_file_qr}' untuk membayar!")
print(Fore.CYAN + "=" * 50)

