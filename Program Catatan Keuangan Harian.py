# Program Catatan Keuangan Harian

pemasukan = 0
pengeluaran = 0

while True:
    print("\n=== CATATAN KEUANGAN HARIAN ===")
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Ringkasan")
    print("4. Keluar")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "1":
        try:
            uang = int(input("Masukkan jumlah pemasukan: "))
            pemasukan += uang
            print("Pemasukan berhasil ditambahkan!")
        except:
            print("Input harus angka!")
    
    elif pilih == "2":
        try:
            uang = int(input("Masukkan jumlah pengeluaran: "))
            pengeluaran += uang
            print("Pengeluaran berhasil ditambahkan!")
        except:
            print("Input harus angka!")
    
    elif pilih == "3":
        saldo = pemasukan - pengeluaran
        print("\n--- RINGKASAN ---")
        print("Total Pemasukan  :", pemasukan)
        print("Total Pengeluaran:", pengeluaran)
        print("Saldo Sekarang   :", saldo)
    
    elif pilih == "4":
        print("Catatan Keuangan selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")