# CHALLENGE MODIFIKASI
# Ubah diskon membernya jadi 20%. Diskon tambahannya dihapus saja.

# Fungsi Diskon Bertingkat
# Tujuan: Menghitung harga akhir berdasarkan member

def cek_diskon(member, total):
    diskon = 0
    # MODIFIKASI: Diskon member jadi 20%, hapus diskon tambahan
    if member.lower() == "ya":
        diskon = 20  # Diskon member 20%
    
    total_diskon = total * diskon / 100
    return total - total_diskon

status_member = input("Apakah Anda member? (Ya/Tidak): ")
total_belanja = float(input("Masukkan total belanja: "))

total_bayar = cek_diskon(status_member, total_belanja)

print(f"Total bayar akhir: Rp {int(total_bayar)}.")
