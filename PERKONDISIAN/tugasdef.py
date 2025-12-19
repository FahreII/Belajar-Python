def option():
    print("\n =========Program Konversi Waktu=========")
    print("pilih salah satu dari tiga")
    print("1. Konversi Jam ke Menit")
    print("2. Konversi Menit ke detik")
    print("3. keluar dari perogram")
    pilihan = int(input("masukan pilihan anda : "))
    return pilihan

def jam_ke_menit(jam):
    hasil_menit = jam * 60
    return hasil_menit

def jam_ke_detik(jam):
    hasil_detik = jam * 3600
    return hasil_detik

pilihan = 0
while pilihan < 3:
    pilihan = option()
    if pilihan == 3:
        print("Kamu telah keluar dari program")
        break
    elif pilihan == 1 or pilihan == 2:
        Jam = int(input("masukan jam : "))
        if pilihan == 1:
            Jam = jam_ke_menit(Jam)
            print("Hasil Konversi Jam adalah {} menit".format(Jam))
        else:
            jam = jam_ke_detik(Jam)
            print("Hasil Konversi jam ke Detik Adalah {}".format(jam))
    else :
        print("Pilihan tidak valid! silahkan masukan 1,2 atau 3.")