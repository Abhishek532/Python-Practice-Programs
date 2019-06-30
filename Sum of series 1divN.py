n=int(input("Enter a number :"))
s=0
for i in range(1,n+1):
    a=1.0/i
    s=s+a
print("Sum is",round(s,3))
