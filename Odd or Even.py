def odd_even(a):
    if a%2==0:
        print(a,"is even")
    elif a%2==1:
        print(a,"is odd")
    else:
        print("Invalid output")
while(1):
    x=int(input("Enter a number :"))
    odd_even(x)
    print("----------------")
