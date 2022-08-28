n=int(input("enter number of rows:"))
i=1
while i<=n:
    j=i
    k=ord("E")
    while j>i:
        print(chr(k),end=" ")
        j=j-1
        k=k+1
    
    i=i+1
    print()


