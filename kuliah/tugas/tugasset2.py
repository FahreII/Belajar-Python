day1 = {"keju", "tepung", "garam", "gula", "coklat"}
day2 = {"garam", "gula", "kecap", "coklat"}

print(day1)
print(day2)
day2.add("keju")
print(day2)
c = day1.intersection(day2)
print(c)
day2.remove("garam") 
d = day1.symmetric_difference(day2)
print(d)
e = day1.difference(day2)
print(e)
