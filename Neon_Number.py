n=int(input())
x=n**2
y=str(x)
L=len(y)
s=0
for i in range(0,L):
    s=s+int(y[i])
if n==s:
    print("Neon Number")
else:
    print("Not Neon Number")
    
    