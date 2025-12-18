# Fungsi Diskon Bertingkat
# Tujuan: Menghitung harga akhir berdasarkan member

def cek_diskon(member, total):
    diskon = 0
    if member.lower() == "ya":
        diskon += 10  # Diskon member 10%
    if total > 1000000:
        diskon += 5  # Diskon ekstra 5% untuk belanja > 1 juta
    
    total_diskon = total * diskon / 100
    return total - total_diskon

status_member = input("Apakah Anda member? (Ya/Tidak): ")
total_belanja = float(input("Masukkan total belanja: "))

total_bayar = cek_diskon(status_member, total_belanja)

print(f"Total bayar akhir: Rp {int(total_bayar)}.")
