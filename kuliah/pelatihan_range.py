a = range(1,8,+3) #melakukan increment dangan penambahan 3
print("Berikut isi variabel a ; {}".format(list(a)))

b = range(10,2,-2) #melakukan increment dangan pengurangan 2
print("Berikut isi variabel b ; {}".format(list(b)))

for i in range (10,2,-2):
    print("isi i adalah {}".format(i))

for i,item in enumerate(range(10,2,-2)):
    print("isi i index {} adalah {}".format(i, item))


for i in range(0,5):
    for j in range(0,i+1):
        print("*", end="")
    print()
# i = 0, j = 0,1

suhu = 0
while suhu < 100:
    print(suhu)
    suhu+=40

