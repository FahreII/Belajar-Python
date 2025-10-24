belanja = int(input("Masukan total belanja anda : "))
diskon = int(input("Masukan diskon : "))

def total_setelah_diskon(belanja,diskon):
    total_setelah_diskon = belanja - (belanja * diskon / 100)
    return total_setelah_diskon
hasil = total_setelah_diskon(belanja, diskon)
print("Nominal setelah diskon {}".format(hasil))