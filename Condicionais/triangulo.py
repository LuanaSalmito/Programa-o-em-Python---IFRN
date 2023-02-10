a, b, c , d= map(int, input().split(" "))
contador = 0
 
#testando o A
if (a < b + c):
    if (a > b and a > c):
        print('S')
        contador = contador + 1
 
if (a < b + d):
    if (a > b and a > d):
        if contador == 0:
            print('S')
            contador = contador + 1
 
if (a < c + d):
    if (a > c and a > d):
        if contador == 0:
            print('S')
            contador = contador + 1
 
#testando o B
 
if (b < a + c):
    if (b > a and b > c):
        if contador == 0:
            print('S')
            contador = contador + 1
 
if (b < a + d):
    if (b > a and b > d):
        if contador == 0:
            print('S')
            contador = contador + 1
 
if (b < c + d):
    if (b > c and b > d):
        if contador == 0:
            print('S')
            contador = contador + 1
 
#testando o C
 
if (c < b + a):
    if (c > b and c > a):
        if contador == 0:
            print('S')
            contador = contador + 1
 
 
if (c < a + d):
    if (c > a and c > d):
        if contador == 0:
            print('S')
            contador = contador + 1
 
 
if (c < b + d):
    if (c > b and c > d):
        if contador == 0:
            print('S')
            contador = contador + 1
            
#testando o D
 
if (d < b + a):
    if (d > b and d > a):
        if contador == 0:
            print('S')
            contador = contador + 1
 
 
if (d < a + c):
    if (d > a and d > c):
        if contador == 0:
            print('S')
            contador = contador + 1
 
 
if (d < b + c):
    if (d > b and d > c):
        if contador == 0:
            print('S')
            contador = contador + 1
 
#sem triângulo
if contador == 0:
    print('N')