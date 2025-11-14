haripertama = {"Mady":8,"Roger":5,"paul":5,"Lucy":7}
print(haripertama)

harikedua = {"Ken":8,"Andre":7,"Smith":6}
print(harikedua)

haripertama.update(harikedua)
print(haripertama)

haripertama["paul"] = 8
haripertama["Roger"] = 8
haripertama["Smith"] = 8
print(haripertama)

for nama,nilai in haripertama.items():
    if nilai >= 8:
        print(nama,nilai)