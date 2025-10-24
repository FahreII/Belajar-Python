
total_nilai = 0

nama = str(input("Masukan nama mahasiswa : "))
jumlah_mk = int(input("Masukan jumlah mata kuliah : "))
for i in range (jumlah_mk):
    nama_mk = str(input("Masukan nama mata kuliah : "))
    nilai = float(input("Masukan nilai (0-100) : "))

    while nilai < 0 or nilai > 100:
        print("Nilai harus antara 0-100!")
        nilai = float(input("Masukan nilai 0 - 100 : "))
    total_nilai += nilai

ipk = total_nilai / jumlah_mk
if ipk > 60:
    status = "LULUS"
else:
    status = "TIDAK LULUS"
print(f"Nama mahasiswa : {nama}")
print(f"Status         : {status}")