t = int(input())
 
for i in range (t):

    contador = 0
    a,b,pa,pb = map(float,input().split(" "))

    a = int(a)
    b = int(b)

    while(a <= b):
        a = int(a * ((pa/100.0)+1))
        if (pb != 0):
            b = int(b * ((pb/100.0)+1))

        contador += 1

        if (contador > 100):
            print("Mais de 1 seculo.")
            break
 
    if(contador <= 100):
        print("{} anos.".format(contador))