def option():
    print("pilih salah satu dari tiga fungsionalistas berilut :")
    print("1. mencari luas persegi panjang")
    print("2. mencari keliling persegi panjang")
    print("3. keluar dari perogram")
    pilihan = int(input("masukan pilihan anda:"))
    return pilihan

def luas_persegi_panjang(panjang,lebar):
    luas = panjang * lebar
    return luas

def keliling_persegi_panjang(panjang,lebar):
    keliling = 2 * (panjang+lebar)
    return keliling

pilihan = 0
while pilihan < 3 :
    pilihan = option()
    if pilihan == 3:
        break
    elif pilihan == 1 or pilihan == 2:
        panjang = int(input("Masukan Panjang :"))
        lebar = int(input("Masukan Lebar :"))

        if pilihan == 1:
            luas = luas_persegi_panjang(panjang, lebar)
            print("Hasil Luas Persegi Panjang Adalah {}".format(luas))
        else:
            keliling = keliling_persegi_panjang(panjang, lebar)
            print("Hasil Luas Persegi Panjang Adalah {}".format(keliling))
    else :
        print("Pilihan tidak valid! silahkan masukan 1,2 atau 3.")