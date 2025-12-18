nilai_mahasiswa = [80, 100, 75]

def print_menu():
    print("\n1. Tambah Nilai Mahasiswa")
    print("2. Tampilkan Nilai Mahasiswa")
    print("3. Tampilkan Nilai Mahasiswa terbesar")
    print("4. Tampilkan Nilai Mahasiswa terkecil")
    print("5. Keluar")

def tambah_nilai_mahasiswa():
    nilai_baru = int(input("\nMasukan nilai baru : "))
    nilai_mahasiswa.append(nilai_baru)

    print("\nNilai berhasil dimasukan")

def tampilkan_nilai_mahasiswa():
    urutan = 1
    for nilai in nilai_mahasiswa:
        print(f"Nilai ke-{urutan}: {nilai}")
        urutan += 1

nilai_mahasiswa = [80, 100, 75]

def tampilkan_nilai_mahasiswa_terbesar():
    nilai_terbesar = nilai_mahasiswa[0]
    for nilai in nilai_mahasiswa:
        if nilai_terbesar < nilai:
            nilai_terbesar = nilai
    print(f"Nilai terbesar adalah {nilai_terbesar}")

def tampilkan_nilai_mahasiswa_terkecil():
    nilai_terkecil = nilai_mahasiswa[0]
    for nilai in nilai_mahasiswa:
        if nilai_terkecil > nilai:
            nilai_terkecil = nilai
    print(f"Nilai terkecil adalah {nilai_terkecil}")

while True:
    print_menu()
    menu = input("Masukan menu [1-5] : ")

    if menu == "1":
        tambah_nilai_mahasiswa()

    elif menu == "2":
        tampilkan_nilai_mahasiswa()

    elif menu == "3":
        tampilkan_nilai_mahasiswa_terbesar()

    elif menu == "4":
        tampilkan_nilai_mahasiswa_terkecil()

    elif menu == "5":
        break

    else:
        print("\nMenu tidak valid")