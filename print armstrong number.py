for i in range(1,10001):
    n=len(str(i))
    sum=0
    i=str(i)
    num=i
    for digit in i:
        sum=sum+int(digit)**n
    if sum==num:
        print(num)
