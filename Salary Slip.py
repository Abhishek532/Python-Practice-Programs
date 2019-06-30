print ("\t\t\t Generate Salary Slip")
print ("---------------------------------------------------------")
name = input("Enter Employee Name ")
bs   = int(input("Enter Employee's Basic Salary "))
hra  = int(input("Enter HRA in % of Basic Salary "))
ta   = int(input("Enter TA in % of Basic Salary "))
da   = int(input("Enter DA in % of Basic Salary "))
it   = int(input("Enter IT in % of Basic Salary "))
pf   = int(input("Enter PF in % of Basic Salary "))

hra_per = hra*bs/100
ta_per  = ta*bs/100
da_per  = da*bs/100
it_per  = it*bs/100
pf_per  = pf*bs/100

print("\t Your HRA is ", hra_per)
print("\t Your TA is ",ta_per)
print("\t Your DA is ",da_per)
print("\t Your IT is ",it_per)
print("\t Your PF is ",pf_per)
print("Your name is ",name)
print("Your salary is ",bs + hra_per + ta_per + da_per - it_per - pf_per)
print ("---------------------------------------------------------")

