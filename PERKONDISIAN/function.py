#contoh fungsi tanpa parameter

def hallo ():
    print("halo world")
hallo()


#dengan parameter
def sapa (nama):
    print("hallo. {}".format (nama))
sapa("parel")


def tambah (a,b):
    hasil = a + b
    print("hasil penjumlahan {}".format(hasil))
tambah(2,4)


def welcome():
    return "selamat datang"
print(welcome())

def sapa (nama):
    return ("Halo, {}".format(nama))
print(sapa("parel"))

def kali (x,y):
    return x * y
hasil = kali(5,5)
print("hasil perkalian adalah {}".format(hasil))



