num_from = int(input("Please input number to go from: "))
num_to = int(input("Please input number to: "))


for i in range(num_from, num_to +1):
  if (i % 2 == 0):
      print(i)

  #else:
  #output_string = ""
  #for num in range(num_from, num_to +1):
    #  output_string += str(num)
