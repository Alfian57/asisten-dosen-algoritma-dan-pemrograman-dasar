# Daftar Belanja Sederhana (List)
# Tujuan: Mengelola daftar belanja

belanjaan = []

print("=== Daftar Belanja ===")
while True:
    print("\n1. Tambah item")
    print("2. Lihat daftar")
    print("3. Selesai")
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == "1":
        item = input("Masukkan nama item: ")
        belanjaan.append(item)
        print(f"'{item}' berhasil ditambahkan.")
    elif pilihan == "2":
        if len(belanjaan) == 0:
            print("Daftar belanja masih kosong.")
        else:
            print("\nDaftar Belanja:")
            for i, item in enumerate(belanjaan, 1):
                print(f"{i}. {item}")
    elif pilihan == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")
