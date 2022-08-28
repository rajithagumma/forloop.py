w=input("enter the word:")
v=len(w)
i=0
while i<v:
    j=i
    while j>1:
        print(w[j],end=" ")
        j=j-1
    i=i+1
    print()
