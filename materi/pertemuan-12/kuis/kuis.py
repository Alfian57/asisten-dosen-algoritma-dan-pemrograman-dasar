# Daftar menu dan harga dasar
MENU = [
    ("Burger", 15000),
    ("Ayam Goreng", 20000),
    ("Minuman", 5000)
]
UPSIZE_HARGA = 5000
PAJAK_PERSEN = 10

while True:
    print("\n=== SELAMAT DATANG DI RESTO KITA ===\n")
    total_belanja = 0
    while True:
        print("[MENU UTAMA]")
        for i, (nama, harga) in enumerate(MENU, 1):
            print(f"{i}. {nama} ({harga//1000}k)")
        print(f"4. Selesai & Bayar")
        try:
            pilihan = int(input("Pilih Menu (1-4): "))
        except ValueError:
            print("Input harus angka 1-4!")
            continue
        if pilihan == 4:
            break
        if pilihan < 1 or pilihan > 4:
            print("Pilihan tidak valid!")
            continue
        nama, harga = MENU[pilihan-1]
        print(f"Anda memilih {nama}.")
        upsize = input("Mau ukuran Large (+5000)? (y/n): ").strip().lower()
        if upsize == 'y':
            harga += UPSIZE_HARGA
            ukuran = "Large"
        else:
            ukuran = "Regular"
        print(f"--> {nama} {ukuran} ({harga}) ditambahkan.")
        total_belanja += harga
        print(f"Subtotal saat ini: Rp {total_belanja:,}")
    # Hitung pajak dan grand total
    pajak = total_belanja * PAJAK_PERSEN // 100
    grand_total = total_belanja + pajak
    print("\n--- STRUK PEMBAYARAN ---")
    print(f"Total Pesanan : Rp {total_belanja:,}")
    print(f"PPN (10%)     : Rp {pajak:>6,}")
    print("-------------------------")
    print(f"GRAND TOTAL   : Rp {grand_total:,}")
    # Proses pembayaran
    while True:
        try:
            uang = int(input("Masukkan Uang: "))
        except ValueError:
            print("Input harus berupa angka!")
            continue
        if uang < grand_total:
            print(f"Uang kurang Rp {grand_total-uang:,}!")
        else:
            print(f"\nKembalian: Rp {uang-grand_total:,}")
            print("Terima kasih!\n")
            break
    # Selesai satu transaksi, tanya apakah ingin transaksi lagi
    lagi = input("Transaksi baru? (y/n): ").strip().lower()
    if lagi != 'y':
        print("Program selesai.")
        break
