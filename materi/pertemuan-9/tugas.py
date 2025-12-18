try:
    # Langkah 1: Minta input jumlah pembayaran dan validasi
    jumlah_input = input("Masukkan jumlah pembayaran: ")
    jumlah = float(jumlah_input)  # Akan ValueError jika bukan angka
    
    # Validasi: cek apakah jumlah >= 1
    if jumlah < 1:
        jumlah = float("tidak_valid")  # Trigger ValueError untuk jumlah tidak valid
    
    # Langkah 2: Baca saldo dari file saldo.txt
    with open("saldo.txt", "r") as file:
        saldo = float(file.read().strip())
    
    # Cek apakah saldo mencukupi
    if saldo < jumlah:
        saldo = 1 / 0  # Trigger ZeroDivisionError untuk saldo tidak cukup
    
    # Langkah 3: Proses pembayaran berhasil
    saldo_baru = saldo - jumlah
    
    # Update saldo di file
    with open("saldo.txt", "w") as file:
        file.write(str(saldo_baru))
    
    # Catat transaksi ke riwayat_transaksi.txt
    with open("riwayat_transaksi.txt", "a") as file:
        file.write(f"Pembayaran: {jumlah}, Saldo tersisa: {saldo_baru}\n")
    
    print(f"Pembayaran berhasil! Saldo Anda sekarang {saldo_baru}")

except ValueError:
    print("Jumlah pembayaran tidak valid")

except ZeroDivisionError:
    print("Saldo Anda tidak cukup untuk melakukan pembayaran")

except FileNotFoundError:
    print("File saldo tidak ditemukan")

finally:
    print("Proses pembayaran selesai")
