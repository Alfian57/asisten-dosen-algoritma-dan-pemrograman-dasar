# CHALLENGE MODIFIKASI
# Tampilkan outputnya hanya Jam dan Menit saja. Detiknya tidak usah ditampilkan.

# Konversi Waktu (Fungsi)
# Tujuan: Mengubah detik menjadi format Jam:Menit:Detik

def format_waktu(detik):
    # Hitung jam
    jam = int(detik / 3600)
    
    # Hitung sisa detik setelah dikurangi jam
    sisa = detik - (jam * 3600)
    
    # Hitung menit dari sisa
    menit = int(sisa / 60)
    
    # Hitung detik akhir
    detik_akhir = sisa - (menit * 60)
    
    return jam, menit, detik_akhir

total_detik = int(input("Masukkan total detik: "))
jam, menit, detik = format_waktu(total_detik)

# MODIFIKASI: Hanya tampilkan jam dan menit
print(f"{jam} jam, {menit} menit.")
