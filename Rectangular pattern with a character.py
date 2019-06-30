def rectangle(n,h,v):
    print("_____________________")
    for i in range(v):
        print(n,end=" ")
        for j in range(h-1):
            print(n,end=" ")
        print()
    print("______________________")

rectangle(5,3,6)

