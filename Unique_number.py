x=int(input())
y=str(x)
L=len(y)
count=0
for i in range(0,L):
    x=y[i]
    for j in range(0,L):
        if x==y[j]:
            count=count+1
if count==L:
    print("Unique Number")
else:
    print("Not Unique Number")