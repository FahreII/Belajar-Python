total_harga = 0
jumlah_pembelian = int(input("Masukan jumlah pembelian : "))
for i in range (jumlah_pembelian):
    nama = str(input("Masukan nama barang : "))
    jumlah = int(input("Masukan jumlah barang anda : "))
    harga = int(input("Masukan harga : "))
    total_harga = total_harga + (harga * jumlah)
bayar = 0
if total_harga > 500000 :
    diskon = total_harga - ( 10 / 100 * total_harga)
    bayar = total_harga
else:
    diskon = total_harga
    bayar = diskon
print("======STRUK=====")
print("uang yang harus dibayar adalah : Rp {}".format(bayar))




