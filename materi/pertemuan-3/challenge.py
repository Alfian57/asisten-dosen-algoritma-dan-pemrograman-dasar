print("===== Sistem Rekomendasi Pakaian =====")
print("1. Pria")
print("2. Wanita")

jenis_kelamin = input("Pilih jenis kelamin [1/2]: ")

if jenis_kelamin == "1":
    tinggi = float(input("Tinggi Badan (cm): "))

    if tinggi < 120:
        print("Tinggi pria di bawah batas minimum.")
    elif tinggi < 165:
        print("Ukuran pakaian yang direkomendasikan: S")
    elif tinggi < 175:
        print("Ukuran pakaian yang direkomendasikan: M")
    elif tinggi < 185:
        print("Ukuran pakaian yang direkomendasikan: L")
    elif tinggi < 250:
        print("Ukuran pakaian yang direkomendasikan: XL")
    else:
        print("Tinggi pria di atas batas maksimal.")

elif jenis_kelamin == "2":
    tinggi = float(input("Tinggi Badan (cm): "))

    if tinggi < 100:
        print("Tinggi wanita di bawah batas minimum.")
    elif tinggi < 155:
        print("Ukuran pakaian yang direkomendasikan: S")
    elif tinggi < 165:
        print("Ukuran pakaian yang direkomendasikan: M")
    elif tinggi < 175:
        print("Ukuran pakaian yang direkomendasikan: L")
    elif tinggi < 230:
        print("Ukuran pakaian yang direkomendasikan: XL")
    else:
        print("Tinggi wanita di atas batas maksimal.")

else:
    print("Pilihan tidak valid. Silakan pilih 1 untuk Pria atau 2 untuk Wanita.")
