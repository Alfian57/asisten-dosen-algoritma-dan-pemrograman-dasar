# ==== TIPE DATA COLLECTION ====
# 1. list
# data bersifat mutable (bisa dirubah)
list_nama = ["alfian", "charles", "kunaka"]

# mengakses
# kita bisa mengakses sebuah list berdasarkan indeks
# indeks dimulai dari angka 0
print(list_nama[2])
list_nama[1] = "daniel"
print(list_nama)
print()

# manambah
# append()
# append digunakan untuk menambahkan data pada akhir list
list_nama.append("Diva")
print(list_nama)
print()

# insert()
# insert digunakan untuk menambahkan data indeks yang spesifik
list_nama.insert(1, "Satya")
print(list_nama)
print()

# menghapus
# pop()
# pop digunakan untuk menghapus data pada akhir list
nama_yang_dihapus = list_nama.pop()
print(f"Nama yang dihapus adalah {nama_yang_dihapus}")
print(list_nama)
print()

# remove()
# remove digunakan untuk menghapus data pada data yang spesifik
list_nama.remove("Satya")
print(list_nama)
print()


list_buah = ["pisang", "apel", "kiwi", "mangga", "sawo"]

# mengurutkan data
# sort
list_buah.sort()
print(list_buah)
print()

# 2. Tuple
# data bersifat immutable (tidak bisa dirubah)
list_nilai = (100, 90, 75, 85)

# error 
# list_nilai[0] = 90

# 3. Dictionary
data_diri = {
    "nama": "Alfian Gading",
    "nim": "5230411121",
    "alamat": "Banguntapan"
}
print(data_diri["nim"])
print(data_diri)
print()

# menambah
# dictionary tidak mamakai append()
data_diri["tanggal lahir"] = "1-1-2004"

# menghapus
del data_diri["alamat"]
print(data_diri)

# mengubah
data_diri["nama"] = "Charles Daniel"
print(data_diri)

# tambahan
print(data_diri.keys())
print(data_diri.values())