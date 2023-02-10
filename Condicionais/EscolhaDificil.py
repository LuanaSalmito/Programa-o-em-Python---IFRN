f, b, m = map(int, input(). split(" "))
rf, rb, rm = map(int, input(). split(" "))
 
geral = 0
if f < rf:
    geral = geral + (-1*(f-rf))
if b < rb:
    geral = geral + (-1*(b-rb))
if m < rm:
    geral = geral + (-1*(m-rm))
print(geral)