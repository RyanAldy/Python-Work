start_number = int(input("Tables From: "))
end_number = int(input("Tables to: "))

for start in range(start_number, end_number +1):
    print("\nTimes Table =" , start)
    for i in range(1,11):
        print(str(start) + " X " + str(i) + " = " + str(start * i))
