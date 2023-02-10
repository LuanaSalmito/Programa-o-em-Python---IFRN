a,b,c = map(int, input().split(" "))
lista_A = []
contador = 0
 
for i in range (c):
    
    if contador == c:
        break
    if contador + a > c:
        break
    
    contador = contador + a
    lista_A.append (contador)
 
contador = 0
lista_B = []
 
for i in range (c):
   
    if contador == c:
        break
    if contador + b > c:
        break
    
    contador = contador + b
    lista_B.append(contador)
 
uniao = list(set(lista_A+lista_B))
soma_total = len(uniao)
print(soma_total)