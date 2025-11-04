list_sampah = [
    {
        "nama pelapor": "Alfian Gading",
        "lokasi": "Banguntapan",
        "jenis sampah": "Organik",
    },
    {
        "nama pelapor": "Charles Daniel",
        "lokasi": "Bekasi",
        "jenis sampah": "Anorganik",
    },
]

def print_menu():
    print("\n\n===== Program Pelaporan Sampah =====")
    print("1. Lihat Laporan Sampah")
    print("2. Tambah Laporan Sampah")
    print("3. Keluar")

def lihat_laporan_sampah():
    print("\n\n===== Laporan =====\n")
    nomor = 1
    for sampah in list_sampah:
        print(f"{nomor}. Laporan sampah di {sampah["lokasi"]} berjenis {sampah["jenis sampah"]} oleh {sampah["nama pelapor"]}")
        nomor += 1

def tambah_laporan_sampah():
    nama_pelapor = input("Masukan nama pelapor\t\t: ")
    lokasi = input("Masukan lokasi\t\t\t: ")
    jenis_sampah = input("Masukan jenis sampah\t\t: ")

    list_sampah.append({
        "nama pelapor": nama_pelapor,
        "lokasi": lokasi,
        "jenis sampah": jenis_sampah,
    })

while True:
    print_menu()
    menu = input("\nMasukan menu [1-3] : ")

    if menu == "1":
        lihat_laporan_sampah()
    elif menu == "2":
        tambah_laporan_sampah()
    elif menu == "3":
        print("\n\n============")
        print("Sampai Jumpa")
        print("============")
        break
    else:
        print("\n\n========================")
        print("Pilihan menu tidak valid")
        print("========================")