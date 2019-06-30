a=int(input("Enter a number :"))
rev=0
while a>0:
    rem=a%10
    a=int(a/10)
    rev=rev*10+rem
print(rev)
    
