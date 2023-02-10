c = int(input())
d = int(input())
t = int(input())
ac = (d/c) - t
if ac<0:
    print(0.0)
else: 
    print(f'{ac:.1f}')