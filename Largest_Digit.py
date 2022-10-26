N=int(input())
L=0
while N>0:
    x=N%10
    if x>L:
        L=x
    N=N//10
print(L)