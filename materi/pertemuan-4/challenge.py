def jam_ke_menit(jam: float):
    menit = jam * 60
    return menit


def menit_ke_detik(menit: float):
    detik = menit * 60
    return detik


def jam_ke_detik(jam: float):
    detik = jam * 3600
    return detik


print("===== Kalkulator Konversi Waktu =====")
print("1. Jam ke Menit")
print("2. Menit ke Detik")
print("3. Jam ke Detik")

waktu = input("Pilih jenis konversi [1/2/3]: ")

if waktu == "1":
    jam = float(input("Masukkan waktu dalam jam: "))
    hasil = jam_ke_menit(jam)
    print(f"Hasil Konversi: {hasil} menit")

elif waktu == "2":
    menit = float(input("Masukkan waktu dalam menit: "))
    hasil = menit_ke_detik(menit)
    print(f"Hasil Konversi: {hasil} detik")

elif waktu == "3":
    jam = float(input("Masukkan waktu dalam jam: "))
    hasil = jam_ke_detik(jam)
    print(f"Hasil Konversi: {hasil} detik")

else:
    print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
