suhu = float(input("Masukan suhu dalam Calcius : "))
F = (suhu* 9/5) + 32
print(f"Suhu dalam Fahrenheit: {F} ")

F = float(input("Masukkan suhu dalam Fahrenheit: "))
suhu = (F - 32) * 5/9
print(f"Suhu dalam Celcius: {suhu:.2f}")
