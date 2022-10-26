n=int(input())
sum=0
p=1
while n>0:
    x=n%10
    sum=sum+x
    p=p*x
    n=n//10
if sum==p:
    print("Spy Number")
else:
    print("Not Spy Number")