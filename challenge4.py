# Print the words in reverse

sentence = str(input("Enter sentence: ")).strip()

word_buffer = ''

char = 0

# first -1 is subtracting 1 from length so index isn't out of bounds,
# second -1 is start point, last -1 is to decrement
for char in range(len(sentence) -1, -1, -1):
    sub_word = sentence[char]
    if sub_word == ' ':
        print(word_buffer)
        word_buffer = ''
    else:
        word_buffer = sub_word + word_buffer

# Need a print here to print the last word as it won't have a space after it
print(word_buffer)
