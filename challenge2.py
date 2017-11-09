# Find specific string in the sentence

sentence = str(input("Please enter sentence: ")).strip()
search_word = str(input("Word to find: "))

word_buffer = ''
#search_word_len = len(search_word)

char = 0
for char in range(len(sentence)):
    sub_word = sentence[char:(char + 1)]
    if sub_word == ' ':
        word_buffer = ''
    else:
        word_buffer = word_buffer + sub_word
        if word_buffer == search_word:
            print("Matched!", " ", word_buffer)
            break
