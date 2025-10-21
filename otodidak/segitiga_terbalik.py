for i in range (5,0,-1):
    for j in range(0,i):
        print("*", end="")
    print()

for i in range(5,0,-1):
    print(" " * (5-i) + "*" * i)