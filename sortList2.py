# Find top 3 in list
a = 0
myList = []

while a != -1:
    a = int(input("Enter number: "))
    if a == -1:
        break
    else:
        myList.append(a)


myList.sort(reverse=True)


max_value = max(myList)
print(max_value)

counter = 0
# Looping through each element of the list and storing in i
for i in myList:
    if i < max_value:
        max_value = i
        print(max_value)
        counter += 1
        # Break out of the for loop if looped through more than twice.
        #Starts at 0 and finishes at 1
        if counter > 1:
            break
