N=int(input())
temp=N
sum=0
n1=str(N)
L=len(n1)
n2=int(N)

while N>0:
    x=N%10
    sum=sum+x**L
    L=L-1
    N=N//10
if sum==temp:
    print("True")
else:
    print("False")
    