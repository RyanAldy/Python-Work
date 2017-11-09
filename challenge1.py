# Find the number of words

word = str(input("Please enter word: ").strip())

word_count = 0
#sub_word = ""

for char in range(len(word)):
    if word[char] == ' ':
        word_count += 1
        #if word[char + 1] == ' ':
            #word_count - 1
            #print(word_count)

print (word_count + 1)
