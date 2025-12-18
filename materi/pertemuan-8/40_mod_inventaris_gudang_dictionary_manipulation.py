# CHALLENGE MODIFIKASI
# Ubah fitur 'Tambah' menjadi 'Kurang' (Barang keluar).

# Inventaris Gudang (Dictionary manipulation)
# Tujuan: Update stok barang

gudang = {
    "Pensil": 10,
    "Buku": 5,
    "Penghapus": 8,
    "Penggaris": 12
}

print("=== Inventaris Gudang ===")
while True:
    print("\n1. Kurang barang (barang keluar)")  # MODIFIKASI: Ganti jadi Kurang
    print("2. Lihat stok")
    print("3. Keluar")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        nama_barang = input("Masukkan nama barang: ")
        jumlah = int(input("Masukkan jumlah yang keluar: "))
        
        if nama_barang in gudang:
            # MODIFIKASI: Operasi kurang (barang keluar)
            gudang[nama_barang] -= jumlah
            print(f"Stok {nama_barang} sekarang: {gudang[nama_barang]}")
        else:
            print(f"Barang '{nama_barang}' tidak ditemukan di gudang.")
    
    elif pilihan == "2":
        print("\n=== Stok Gudang ===")
        for barang, stok in gudang.items():
            print(f"{barang}: {stok}")
    
    elif pilihan == "3":
        print("Terima kasih!")
        break
    
    else:
        print("Pilihan tidak valid.")
