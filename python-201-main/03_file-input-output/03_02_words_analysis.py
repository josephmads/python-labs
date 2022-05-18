# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

words_list = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words_list.append(word)

shortest_word = []

for w in words_list:
    if len(w) < 3:
        shortest_word.append(w)

print(shortest_word)

longest_word = []

for w in words_list:
    if len(w) > 20:
        longest_word.append(w)
        
print(longest_word)
    