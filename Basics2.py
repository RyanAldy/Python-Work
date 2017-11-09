phy = int(input("Please enter Physics mark:"))
chem = int(input("Please enter Chemistry mark:"))
maths = int(input("Please enter Maths mark:"))

total = phy + chem + maths
percentage = int((total/300) * 100)

print('-----------------------------')
print("Physics mark: ", phy)
print("Chemistry mark: ", chem)
print("Maths mark: ", maths)
print('-----------------------------')
print("Total marks: ", total )
print("Percentage %: ", percentage)
print('-----------------------------')
