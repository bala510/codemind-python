x=int(input())
b=""
for i in range(0,x):
    if i*(i+1)==x:
        b="True"
if b=="True":
    print("YES")
else:
    print("NO")