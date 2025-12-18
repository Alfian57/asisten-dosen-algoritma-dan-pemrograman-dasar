list_barang = {
    "pensil": 5000,
    "penggaris": 2000,
    "buku": 10000,
}

def tambah_barang():
    nama_barang = input("Masukan nama barang : ")
    harga_barang = int(input("Masukan harga barang : "))

    list_barang[nama_barang] = harga_barang
    print("Barang berhasil ditambahkan")