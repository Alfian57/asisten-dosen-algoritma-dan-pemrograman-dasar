def kalkulator_pembelian(list_barang):
    nama_barang = input("Masukan nama barang yang ingin di beli : ")
    jumlah_barang = int(input("Masukan jumlah barang yang ingin di beli : "))

    harga = list_barang[nama_barang]
    total_harga = harga * jumlah_barang

    print(f"Jumlah harga yang dibayarkan adalah RP.{total_harga}")