nama = int(input("Berapa jumlah nama yang akan dimasukan ? "))
daftar_nama = []

for i in range(nama):
    a = str(input("Masukan nama ke-{} : ".format(i)))
    daftar_nama.append(a)

try:
    data = int(input("Panggil nama dengan index : "))
    print("nama pada index {} adalah {}".format(data,daftar_nama[data]))
except IndexError:
    print("Index ini tidak tersedia")
except ValueError:
    print("Harus berupa angka")


