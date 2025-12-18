pengguna = [
    {
        "nip": "12345",
        "username": "admin",
        "password": "admin",
    }
]

def masuk(username_input, password_input) -> bool:
    for item in pengguna:
        if item["username"] == username_input and item["password"] == password_input:
            return True
    return False

def daftar(nip_input, username_input, password_input) -> None:
    pengguna.append({
        "nip": nip_input,
        "username": username_input,
        "password": password_input,
    })

def hitung_bruto(gaji_bulanan) -> int:
    return gaji_bulanan * 12

def hitung_pengurang_biaya_jabatan(penghasilan_bruto) -> int:
    pengurang = penghasilan_bruto * 5 /100
    if pengurang >= 6000000:
        return 6000000
    return pengurang

def hitung_neto(penghasilan_bruto, pengurang_biaya_jabatan) -> int:
    return penghasilan_bruto - pengurang_biaya_jabatan

def hitung_ptkp(status_pernikahan, jumlah_tanggungan) -> int:
    ptkp = 54000000

    if status_pernikahan == "menikah":
        ptkp += 4500000
    biaya_tanggungan = 4500000 * jumlah_tanggungan
    ptkp += biaya_tanggungan
    return ptkp

def hitung_pkp(penghasilan_neto, ptkp) -> int:
    pkp = penghasilan_neto - ptkp

    if pkp <= 0:
        return 0
    return pkp

def hitung_tarif_progresif(pkp) -> int:
    tarif = 0
    sisa_pkp = pkp

    # Lapisan 5: > 5 Miliar (35%)
    if sisa_pkp > 5000000000:
        tarif += (sisa_pkp - 5000000000) * 0.35
        sisa_pkp = 5000000000

    # Lapisan 4: > 500 Juta - 5 Miliar (30%)
    if sisa_pkp > 500000000:
        tarif += (sisa_pkp - 500000000) * 0.30
        sisa_pkp = 500000000

    # Lapisan 3: > 250 Juta - 500 Juta (25%)
    if sisa_pkp > 250000000:
        tarif += (sisa_pkp - 250000000) * 0.25
        sisa_pkp = 250000000

    # Lapisan 2: > 60 Juta - 250 Juta (15%)
    if sisa_pkp > 60000000:
        tarif += (sisa_pkp - 60000000) * 0.15
        sisa_pkp = 60000000

    # Lapisan 1: 0 - 60 Juta (5%)
    if sisa_pkp > 0:
        tarif += sisa_pkp * 0.05

    return int(tarif)

while True:
    print("\n\nKalkulator PPh 21 Sederhana")
    print("1. Masuk")
    print("2. Daftar")
    print("3. Keluar")
    menu_tamu = input("\nMasukan menu [1-3] : ")

    if menu_tamu == "1":
        username_input = input("Masukan username : ")
        password_input = input("Masukan password : ")

        if masuk(username_input, password_input):
            gaji_bulanan = int(input("\n\nMasukan gaji bulanan : "))
            status_pernikahan = input("Masukan status pernikahan [menikah/belum menikah] : ")
            jumlah_tanggungan = int(input("Masukan jumlah tanggungan : "))

            penghasilan_bruto = hitung_bruto(gaji_bulanan)
            pengurang_biaya_jabatan = hitung_pengurang_biaya_jabatan(penghasilan_bruto)
            penghasilan_neto = hitung_neto(penghasilan_bruto, pengurang_biaya_jabatan)
            ptkp = hitung_ptkp(status_pernikahan, jumlah_tanggungan)
            pkp = hitung_pkp(penghasilan_neto, ptkp)
            tarif_progresif = hitung_tarif_progresif(pkp)

            print("\n\n========================")
            print("Hasil Perhitungan PPh 21")
            print("========================")
            print(f"Penghasilan Bruto\t: {penghasilan_bruto}")
            print(f"Pengurang Biaya Jabatan\t: {pengurang_biaya_jabatan}")
            print(f"Penghasilan Neto\t: {penghasilan_neto}")
            print(f"PTKP\t\t\t: {ptkp}")
            print(f"PKP\t\t\t: {pkp}")
            print(f"PPh 21 Terutang\t\t: {tarif_progresif}")

            break
        else:
            print("\n\n============================")
            print("Username atau password salah")
            print("============================")

    elif menu_tamu == "2":
        nip_input = input("Masukan NIP : ")
        username_input = input("Masukan username : ")
        password_input = input("Masukan password : ")

        daftar(nip_input, username_input, password_input)

        print("\n\n===================")
        print("Registrasi Berhasil")
        print("===================")
    
    elif menu_tamu == "3":
        print("\n\n============")
        print("Sampai Jumpa")
        print("============")
        break
    
    else:
        print("\n\n========================")
        print("Pilihan menu tidak valid")
        print("========================")
