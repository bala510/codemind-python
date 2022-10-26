N=int(input())
y=N**2
rev=0
while N>0:
    x=N%10
    rev=rev*10+x
    N=N//10
N2=rev
y2=N2**2
rev2=0
while y2>0:
    x1=y2%10
    rev2=rev2*10+x1
    y2=y2//10
z=rev2
if y==z:
    print("True")
else:
    print("False")
    
    
    
    