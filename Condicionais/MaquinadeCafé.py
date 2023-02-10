

a1= int(input())
a2= int(input())
a3= int(input())
tandar1= (a2*2)+(a3*4)
tandar2= (a1*2)+(a3*2)
tandar3= (a1*4)+(a2*2)
contador = 0 
if tandar1 <= tandar2 and tandar1 <= tandar3:
    contador = contador + 1
    print(tandar1)
if tandar2 <= tandar1 and tandar2 <= tandar3:
    if contador == 0:
        print(tandar2)
        contador = contador + 1
if tandar3 <= tandar1 and tandar3 <= tandar2:
    if contador == 0:
        print(tandar3)
        contador = contador + 1