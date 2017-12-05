# Count words in a file
words_list = []

with open ("C:\\Users\\Admin\\Documents\\python_test.txt", "r") as file:
    for line in file:
        words_list.extend(line.split())

print(len(words_list))
#print(words_list)
