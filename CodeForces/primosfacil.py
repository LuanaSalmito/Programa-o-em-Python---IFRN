a = int(input())
teste = 0
 
for i in range (1, a+1):
 
    if a % i == 0:
        teste += 1
 
if teste == 2:
    print("Sim")
else:
    print("Nao")