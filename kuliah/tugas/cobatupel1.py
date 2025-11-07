day1 = ("Lukman", "Andi", "Soleh", "Putri")
day2 = ("Soleh", "Putri", "Lukman","Andi")

print(day1)
print(day2)

print(day1[2])

gabung = day1 + day2
print(gabung)
print(gabung.count("Putri"))


print("Lukman" in day2)
print("Andi" in gabung)

for data in gabung:
    print(data)
