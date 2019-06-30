n=int(input("Enter a number :"))
s=0
for i in range(1,n+1):
    if i%2==0:
        a=i**2
        s=s+a
print("Sum is :",s)
