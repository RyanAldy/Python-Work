
sentence = str(input("Please enter sentence: ")).strip()

word_buffer = ''
word_count = 0

for char in range(len(sentence)):
    sub_word = sentence[char]
    if sub_word == ' ':
        print(word_buffer)
        word_count += 1
        word_buffer = ''
    else:
        word_buffer = word_buffer + sub_word

if word_buffer != ' ':
    print(word_buffer, word_count + 1)
