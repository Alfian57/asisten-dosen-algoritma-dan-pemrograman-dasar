# CHALLENGE MODIFIKASI
# Cek khusus jika x=0 dan y=0, tampilkan 'Titik Pusat'.

# Menentukan Kuadran Koordinat
# Tujuan: Menentukan posisi titik (x,y) dalam kartesius

x = float(input("Masukkan nilai x: "))
y = float(input("Masukkan nilai y: "))

# MODIFIKASI: Tambahkan kondisi untuk titik pusat di awal
if x == 0 and y == 0:
    kuadran = "Titik Pusat"
elif x > 0 and y > 0:
    kuadran = "Kuadran I"
elif x < 0 and y > 0:
    kuadran = "Kuadran II"
elif x < 0 and y < 0:
    kuadran = "Kuadran III"
elif x > 0 and y < 0:
    kuadran = "Kuadran IV"
else:
    kuadran = "Titik berada di sumbu"

print(f"Titik berada di {kuadran}")
