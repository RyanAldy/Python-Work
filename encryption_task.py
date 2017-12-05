# Encryption task

encrypted_output = ''

with open ("C:\\Users\\Admin\\Documents\\python_test.txt", "r") as file:
    for line in file:
        words_list = []
        for i in range(len(line)):
                words_list.extend(line[i].split())

# Using ascii characters range to substitute characters
for i in range(len(words_list)):
    if words_list[i].isupper():
        encrypted_output += chr(ord(words_list[i]) - 30)
    elif words_list[i].islower():
        encrypted_output += chr(ord(words_list[i]) - 64)
    else:
        encrypted_output += chr(ord(words_list[i]) - 15)



print('Encrypted output =' , encrypted_output)
print('Decrypted output = ' , (line))
