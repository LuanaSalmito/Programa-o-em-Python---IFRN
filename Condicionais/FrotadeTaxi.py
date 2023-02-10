a, g, ra, rg = map(float, input(). split(" "))
ca = ra/a
cg = rg/g
if (ca > cg):
    print("A")
if (cg > ca or ca==cg):
    print("G")