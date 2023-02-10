c , q  = map(int,input().split(" "))
q = float(q)
cq = (4.00 * q)
xs = (4.50 * q)
xb = (5.00 * q) 
ts = (2.00 * q) 
rf = (1.50 * q)
if c ==1:
    print("Total: R$ {:.2f}". format(cq))
if c == 2:
    print("Total: R$ {:.2f}". format(xs))
if c == 3:
    print("Total: R$ {:.2f}". format(xb))
if c == 4:
    print("Total: R$ {:.2f}". format(ts))
if c ==5:
    print("Total: R$ {:.2f}". format(rf))