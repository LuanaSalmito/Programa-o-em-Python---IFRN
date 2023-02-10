a = int(input())
lista_A = []
 
for i in range (1, a+1):
    if a % i == 0:
        lista_A.append(i)
 
print(*lista_A)