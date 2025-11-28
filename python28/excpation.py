# try:
#     10 * (10/0)
# except ZeroDivisionError:
#     print("pembagian dengan nol tiak diperbolehkan")

# # file = open('data_saya.txt', 'r')

# try:
#     file = open('data_saya.txt','r')
# except FileNotFoundError:
#     print("File tidak ditemukan.")

# try:
#     umur = int(input("Masukan umur : "))
# except ValueError:
#     print("hanya dapat memasukan angka")


# try:
#     umur = int(input("Masukan umur : "))
#     print("umur kamu {} Tahun").format(umur)
# except ValueError:
#     print("hanya dapat memasukan angka")


# try:
#     dictionary = {"satu" : 1, "dua":2}
#     print(dictionary ["tiga"])
# except KeyError:
#     print("key dictory tidak tersedia")

# try:
#     data = [10, 20, 30]
#     idx = int(input("masukan index (0-2) : "))
#     print("Isi list: ", data[idx])
# except IndexError:
#     print("Index tidak tersedia")
# except ValueError:
#     print("index harus berupa angka")

# try:
#     a = 10 * "lima"
#     raise NameError("error type")
# except NameError:
#     print("tipe data error")
#     raise