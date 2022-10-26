x=int(input())
if x>0:
    y=str(x)
    z=len(y)
    u=""
    for i in range(z-1,-1,-1):
        u=u+y[i]
    print(int(u))
else:
    x=(-1)*(x)
    y=str(x)
    z=len(y)
    u=""
    for i in range(z-1,-1,-1):
        u=u+y[i]
    d=int(u)
    print(-d)