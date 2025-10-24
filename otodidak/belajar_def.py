def tambah(a, b):
    return a + b

hasil = tambah(5, 3)
print(hasil)

def konversi_suhu(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
hasil = konversi_suhu(30)
print(f"Suhu 30°C = {hasil}°F")

def total_setelah_diskon(total_belanja,persen_diskon):
    total_setelah_diskon = total_belanja-(total_belanja * persen_diskon / 100)
    return total_setelah_diskon

hasil = total_setelah_diskon(200000, 10)
print(f"Total setelah diskon: {hasil}")