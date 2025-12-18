def penjumlahan(angka_pertama, angka_kedua):
    return angka_pertama + angka_kedua




# Siapkan data
input_1 = 10
input_2 = 5
hasil_yang_diharapkan = 15

# B. Eksekusi
hasil_aktual = penjumlahan(input_1, input_2) # 5

# C. ASSERT
if hasil_aktual == hasil_yang_diharapkan:
    print("✅ STATUS: PASS (Berhasil)")
    print("   Fungsi berjalan sesuai harapan.")
else:
    print("❌ STATUS: FAILED (Gagal)")
    print("   Ada bug di dalam fungsi 'penjumlahan'")

print("--- Test Selesai ---")