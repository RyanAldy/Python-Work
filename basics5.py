try:
    phy = int(input("Please enter Physics mark: "))
    chem = int(input("Please enter Chemistry mark: "))
    maths = int(input("Please enter Maths mark: "))
except Exception as E:
    print("Input must be numeric!")


total = phy + chem + maths
percentage = int((total/300) * 100)
grade = ""

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage < 60:
    grade = "Fail"

print('-----------------------------')
print("Total marks: ", total)
print("Percentage %: ", percentage)
print('-----------------------------')
print("Grade: ", grade)
