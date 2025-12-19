phi = 3.14
def luas_lingkaran(r):
    luas = phi * r * r
    return luas

def keliling_lingkaran(r):
    keliling = phi * (r*2)
    return keliling

def volume_balok(p,l,t):
    hasil = p * l * t
    return hasil
hitung_volume = volume_balok(13,16,30)

def luas_permukaan_kubus (s):
    luas_luas = 6 * s * s
    return luas_luas
hitung_luas = luas_permukaan_kubus(30)



hitung_luas = luas_lingkaran(10)
hitung_keliling = keliling_lingkaran(50)
print("luas lingkaran adalah {}".format(hitung_luas))
print("kelilig lingkaran adalh {}".format(hitung_keliling))
print("Volume balok adalah {}".format(hitung_volume))
print("hasil perkalian adalah {}".format(hitung_luas))

