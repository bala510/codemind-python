x=int(input())
y=int(input())
sum1=0
for i in range(1,x):
    if x%i==0:
        sum1=sum1+i
sum2=0
for i in range(1,y):
    if y%i==0:
        sum2=sum2+i
if sum1==y and sum2==x :
    print("Amicable")
else:
    print("Not Amicable")
