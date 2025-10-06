# ===== ATURAN PENULISAN VARIABLE =====

# 1. Tidak boleh menggunakan spasi
# contoh salah
# nama lengkap = "Alfian Gading"
# contoh benar
# nama_lengkap = "Alfian Gading"

# 2. Tidak boleh diawali dengan angka
# contoh salah
# 1nama = "Alfian Gading"
# contoh benar
# nama1 = "Alfian Gading"
# na2ma = "Alfian Gading"

# 3. Tidak boleh keyword yang ada di python
# contoh salah
# True = "hdjksahd"
# False = "hdjksahd"
# if = "hdjksahd"

# 4. Tidak boleh menggunakan simbol apapun
# kecuali, underscore (_)
# contoh salah
# nama-lengkap = "Alfian Gading"
# nama$lengkap = "Alfian Gading"
# contoh benar
# nama_lengkap = "Alfian Gading"


# ===== GAYA PENULISAN VARIABLE =====
# 1. snake_case
# semuanya huruf kecil
# setiap kata dipisah menggunakan underscore
# nama_lengkap, keranjang_buah_apel

# 2. camelCase
# huruf kapital untuk setiap kata,
# kecuali kata pertama
# namaLengkap, keranjangBuahApel

# 3. PascalCase
# huruf kapital untuk setiap kata
# NamaLengkap, KeranjangBuahApel

# 4. UPPER_CASE / SCREAMING_SNAKE_CASE
# semuanya huruf kapital
# setiap kata dipisah menggunakan underscore
# NAMA_LENGKAP, KERANJANG_BUAH_APEL

# ===== CONCATENATE/MENGGABUNGKAN STRING =====
# print("kelas" + " " + "alpro")

# makanan = "buah apel"
# print("Saya makan" + " " + makanan)

# nama = "Alfian"
# nim = "5230411121"
# print("Nama saya adalah " + nama + " dengan nim " + nim)


# ===== TYPE CASTING =====
# # 1. ke integer
# # int()
# angka_pertama = "10"
# angka_kedua = "10"
# print(int(angka_pertama) + int(angka_kedua))

# # 2. ke float
# # float()
# angka_pertama = "10.5"
# angka_kedua = "10.3"
# print(float(angka_pertama) + float(angka_kedua))

# # 3. ke string
# # str()
# angka_pertama = 1
# angka_kedua = 1.5
# print(str(angka_pertama) + str(angka_kedua))

# 4. ke boolean
# bool()
# string ke boolean
# boolean_pertama = "apel"
# boolean_kedua = "pisang"
# boolean_ketiga = ""
# print(bool(boolean_pertama))
# print(bool(boolean_kedua))
# print(bool(boolean_ketiga))

# integer ke boolean
# boolean_pertama = 23
# boolean_kedua = 0
# boolean_ketiga = -23
# print(bool(boolean_pertama))
# print(bool(boolean_kedua))
# print(bool(boolean_ketiga))

# float ke boolean
# boolean_pertama = 23.5
# boolean_kedua = 0
# boolean_ketiga = -23.5
# print(bool(boolean_pertama))
# print(bool(boolean_kedua))
# print(bool(boolean_ketiga))



# ===== input() =====
# angka_pertama = input("masukan angka pertama : ")
# angka_kedua = input("masukan angka kedua : ")
# hasil = angka_pertama + angka_kedua
# print("user memasukan angka : " + hasil)