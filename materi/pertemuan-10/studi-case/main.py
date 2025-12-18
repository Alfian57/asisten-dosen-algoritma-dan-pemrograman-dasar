while True:
    print("===Data Mahasiswa===")
    print("1. Tambah Data")
    print("2. Lihat Semua Data")
    print("3. Keluar")
    menu = input("Masukan menu [1-3] : ")

    if menu == '1':
        nama_mahasiswa = input("Masukan nama mahasiswa: ")

        with open("data_mahasiswa.txt", "a") as file:
            file.write(nama_mahasiswa + "\n")

    elif menu == '2':
        with open("data_mahasiswa.txt", "r") as file:
            data_mahasiswa = file.readlines()
            print("Daftar Mahasiswa:")
            for nama in data_mahasiswa:
                print(f"{nama}")

    elif menu == '3':
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Menu tidak valid, silakan coba lagi.")