a = int(input())
soma_pares = 0
soma_impares = 0

while a > 0:
    if a % 2 == 0:
        soma_pares +=1
    else:
        soma_impares +=1
        
    a = int(input())

print(soma_pares)
print(soma_impares)