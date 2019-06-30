a = int(input("Enter your marks out of 100 :"))

if 100>=a>89:
    print("Your grade is A")
elif 89>=a>79:
    print("Your grade is B")
elif 79>=a>69:
    print("Your grade is C+")
elif 69>=a>59:
    print("Your grade is C-")
elif 59>=a>33:
    print("You have passed")
elif a<33:
    print("You have failed")
elif a>100:
    print("Invalid input")
else:
    print("Invalid input")

