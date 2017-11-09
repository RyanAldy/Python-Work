try:
    phy = int(input("Please enter Physics mark:"))
    chem = int(input("Please enter Chemistry mark:"))
    maths = int(input("Please enter Maths mark:"))
except Exception as E:
    print("Input must be numeric!")

fail_count = 0

if phy < 60:
    fail_count += 1
if chem < 60:
    fail_count += 1
if maths < 60:
    fail_count += 1

if fail_count == 0:
    print("You have passed!")
elif fail_count == 1:
    print("Retake the exam!")
elif fail_count == 2:
    print("Repeat the course!")
elif fail_count == 3:
    print("Go home!")
