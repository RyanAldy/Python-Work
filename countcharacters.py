# Count characters in text

text = input("Please enter sentence: ")

upper_char_counter = [0] * 26
lower_char_counter = [0] * 26


upper_char_start = ord('A')
#upper_char_end = ord('Z')

lower_char_start = ord('a')
#lower_char_end = ord('z')

# char is now a variable of each item in text/input sentence (essentially an array)
for char in text:
    if char.isupper():
        upper_char_counter[ord(char) - upper_char_start] += 1
    elif char.islower():
        lower_char_counter[ord(char) - lower_char_start] += 1

for i in range(26):
    if upper_char_counter[i] > 0:
        print(chr(upper_char_start + i), ": ", upper_char_counter[i])
    if lower_char_counter[i] > 0:
        print(chr(lower_char_start + i), ": ", lower_char_counter[i])
