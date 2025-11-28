try:
    angka1 = int(input("Masukan angka pertama: "))
    angka2 = int(input("Masukan angka kedua: "))
    bagi = angka1 /angka2
    print("Hasil pembagian adalah : {}").format(bagi)
except ZeroDivisionError:
    print("Tidak boleh dibagi dengan nol")
except ValueError:
    print("Cuma bisa angka")