def lallysum(x,y):
    return x+y
def lallysub(x,y):
    return x-y
def lallydiv(x,y):
    if y==0:
        print("Division by zero not possible")
    else:
        return round(x/y,2)
def lallymul(x,y):
    return x*y

choice=0

while (1):
    print ("Choices : \n\n1.Addition \n2.Subtraction \n3.Division \n4.Multiplication \n\n5.Exit")
    choice = int(input("\nEnter your choice(1-5):"))
    if choice==5:
        break
    a=int(input("\nEnter your first number :"))
    b=int(input("Enter your second number :"))
    if choice==1:
        print("\nSum is",lallysum(a,b))
    elif choice==2:
        print("\nDifference is",lallysub(a,b))
    elif choice==3:
        print("\nQuotient is",lallydiv(a,b))
    elif choice==4:
        print("\nProduct is",lallymul(a,b))
    print("\n1.Exit \n2.Next Operation")
    choice2=int(input("\nEnter your choice(1-2):"))
    if choice2==1:
        break
    elif choice2==2:
        print("------------------------------")
        continue
    else:
        print("Invalid input")
    print("------------------------------")


