def perfect_number(num):
    temp=num
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==temp:
        return True
    else:
        return False
x=int(input())
print(perfect_number(x))
    