a,b = map(int, input().split(" "))
x = 0
 
for i in range (b):
    if x == b:
        break
    if x + a > b:
        break
 
    x = x + a
    print(x)