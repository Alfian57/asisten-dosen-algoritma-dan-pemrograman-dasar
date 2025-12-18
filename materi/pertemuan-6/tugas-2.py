data_diri = ("Alfian Gading", "5230411121", "Informatika")
nilai_mk = {
    "Kalulus": 85,
    "Logika Informatika": 90,
    "Alpro": 88
}

# Menampilkan nama dan jurusan dari data_diri
print(f"Nama: {data_diri[0]}")
print(f"Jurusan: {data_diri[2]}")

# Menampilkan semua nilai mata kuliah dari nilai_mk
print(nilai_mk.values())

# Menambahkan nilai Bahasa Inggris dengan nilai 88
nilai_mk["Bahasa Inggris"] = 88

# Mengubah nilai Kalkulus menjadi 82
nilai_mk["Kalkulus"] = 82

# Menampilkan seluruh isi dictionary nilai_mk
print(nilai_mk)