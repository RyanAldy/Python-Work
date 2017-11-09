# Print sentence to upper, lower, digits * 2 and special chracters as is

sentence = input("Please enter word: ")

word_buffer = ''
char = 0

for char in range(len(sentence)):
    sub_word = sentence[char]
    if sub_word.islower():
        sub_word = sub_word.upper()
        word_buffer += sub_word
        #print(sub_word)
    elif sub_word.isupper():
        sub_word = sub_word.lower()
        word_buffer += sub_word
        #print(sub_word)
    elif sub_word.isdigit():
        sub_word = int(sub_word) * 2
        word_buffer += str(sub_word)
        #print (str(sub_word))
    else:
        word_buffer += sub_word

print(word_buffer)
