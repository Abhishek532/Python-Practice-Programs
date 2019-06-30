def reverse(a):
    rev=0
    while a>0:
        rem=a%10
        a=int(a/10)
        rev=rev*10+rem
    print(rev)

def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)

def fibonacci(a):
    f=0
    s=1
    if a==0:
        print("0")
    elif a==1:
        print("0\n1")
    elif a>1:
        print("0\n1")
    for i in range(0,a):
        n=f+s
        f=s
        s=n
        print(n)

def table(a):
    for i in range(1,11):
        print(a,"x",i,"=",a*i)



while(1):
    print("Choices : \n\n1.Reverse of a number \n2.Factorial of a number \n3.Fibonacci series upto n terms \n4.Table of a number \n\n5.Exit")
    choice=int(input("\nEnter your choice(1-5):"))
    if choice==5:
        print("-----------------------------")
        break
    num=int(input("\nEnter your number :"))
    if choice==1:
        reverse(num)
    elif choice==2:
        factorial(num)
    elif choice==3:
        fibonacci(num)
    elif choice==4:
        table(num)
    print("\n1.Exit \n2.Next Operation")
    choice2=int(input("Enter your choice(1-2) :"))
    if choice2==1:
        print("-----------------------------")
        break
    elif choice2==2:
        print("-----------------------------")
        continue
    else:
        print("Invalid input")
    print("-----------------------------")
    
    


        


    
    

