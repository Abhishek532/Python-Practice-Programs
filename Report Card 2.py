print ("\t\t\t Report Card")
print ("-------------------------------------------------------")
name = input("\tEnter Name ")
rollno = input("\tEnter Rollno ")
address = input("\tEnter Address ")
fath_name = input("\tEnter Father's Name ")
moth_name = input("\tEnter Mother's Name ")
sex = input ("\tEnter Sex ")
marks_pbi = input("\tEnter marks of Punjabi ")
marks_hdi = input("\tEnter marks of Hindi ")
marks_mth = input("\tEnter marks of Maths ")
marks_sci = input("\tEnter marks of Science ")
marks_eng = input("\tEnter marks of English ")
print("\t\t Your name is : ",name)
print("\t\t Your rollnumber is : ",rollno)
print("\t\t Your address is : ",address)
print("\t\t Your father's name is : ",fath_name)
print("\t\t Your mother's name is : ",moth_name)
print("\t\t Your sex is : ",sex)
print("\t\t Your marks in Punjabi : ",marks_pbi)
print("\t\t Your marks in Hindi : ",marks_hdi)
print("\t\t Your marks in Maths : ",marks_mth)
print("\t\t Your marks in Science : ",marks_sci)
print("\t\t Your marks in English : ",marks_eng)

marks_obt = int(marks_pbi) + int(marks_hdi) + int(marks_mth) + int(marks_sci) + int(marks_eng)

print("\t\t Your total marks : ",int(marks_obt),"/500")
print("\t\t Your Percentage is : ",int(marks_obt)/5)
print ("-------------------------------------------------------")
