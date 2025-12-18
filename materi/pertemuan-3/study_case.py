print("===== Sistem Pengiriman Paket =====")
print("1. Yogyakarta")
print("2. Bandung")
print("3. Surabaya")

kota_tujuan = input("Pilih kota tujuan [1/2/3]: ")

if kota_tujuan == "1":
    berat_paket = float(input("Masukkan berat paket (KG): "))
    if berat_paket <= 0:
        print("Berat paket tidak valid.")
    elif berat_paket <= 1:
        print("Biaya pengiriman adalah: Rp 10.000")
    elif berat_paket <= 5:
        print("Biaya pengiriman adalah: Rp 25.000")
    else:
        print("Biaya pengiriman adalah: Rp 50.000")

elif kota_tujuan == "2":
    berat_paket = float(input("Masukkan berat paket (KG): "))
    if berat_paket <= 0:
        print("Berat paket tidak valid.")
    elif berat_paket <= 1:
        print("Biaya pengiriman adalah: Rp 12.000")
    else:
        print("Biaya pengiriman adalah: Rp 30.000")

elif kota_tujuan == "3":
    berat_paket = float(input("Masukkan berat paket (KG): "))
    if berat_paket <= 0:
        print("Berat paket tidak valid.")
    elif berat_paket <= 2:
        print("Biaya pengiriman adalah: Rp 20.000")
    elif berat_paket <= 10:
        print("Biaya pengiriman adalah: Rp 80.000")
    else:
        print("Biaya pengiriman adalah: Rp 100.000")

else:
    print("Input tidak valid.")
