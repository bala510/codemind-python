x=int(input())
y=x**2 
a=str(x)
b=str(y)
L1=len(a)
L2=len(b)
last_part=b[-L1:]
if a==last_part:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
