a,b= map(int, input().split(" "))
lista_A = []
contador = 0
 
for i in range (b):
    
    if contador == b:
        break
    if contador + a > b:
        break
    
    contador = contador + a
    lista_A.append (contador)
 
lista_A.sort(reverse=True)
print(*lista_A)