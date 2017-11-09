# Print the words vertically

sentence = str(input("Enter sentence: "))

word_buffer = ''

char = 0

for char in range(len(sentence)):
    sub_word = sentence[char]
    if sub_word == ' ':
        print(word_buffer)
        word_buffer = ''
    else:
        word_buffer = word_buffer + sub_word

print(word_buffer)
