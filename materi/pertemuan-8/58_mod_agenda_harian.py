# CHALLENGE MODIFIKASI
# Ganti mata pelajaran hari 'Senin' jadi 'Libur'.

# Agenda Harian
# Tujuan: Menampilkan jadwal berdasarkan hari

jadwal = {
    'Senin': 'Libur',  # MODIFIKASI: Ganti jadi Libur
    'Selasa': 'Fisika',
    'Rabu': 'Kimia',
    'Kamis': 'Biologi',
    'Jumat': 'Bahasa Indonesia',
    'Sabtu': 'Olahraga'
}

hari = input("Masukkan hari: ")

if hari in jadwal:
    print(f"Jadwal hari {hari} adalah {jadwal[hari]}")
else:
    print("Hari tidak ditemukan dalam jadwal")
