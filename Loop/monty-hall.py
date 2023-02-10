n = int(input())
contador = 0

for i in range (n):

    temp = int(input())
    if(temp == 2 or temp == 3):
        contador = contador + 1
    
print(contador)