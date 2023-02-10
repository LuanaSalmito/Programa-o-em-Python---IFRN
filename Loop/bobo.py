n = int(input())

j = []

contador = 0

for i in range (n):
    j.append(int(input()))
    if (j[0] < j[i]):
        print("N")
        contador = 1
        break

if (contador == 0):
    print("S")