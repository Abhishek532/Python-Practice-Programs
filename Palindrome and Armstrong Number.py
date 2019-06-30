for i in range(101):
    rev=0
    b=i
    while i>0:
        rem=i%10
        i=int(i/10)
        rev=rev*10+rem
    if b==rev:
        print(b,"is a Palindrome")

print("------------------")


for a in range(1000):  
    n=a                
    b=int(a/10)         
    first=int(b/10)     
    second=int(b-10*first) 
    third=a%10
    if first**3 + second**3 +third**3 == n:
        print(n,"is an Armstrong Number")


    

        


