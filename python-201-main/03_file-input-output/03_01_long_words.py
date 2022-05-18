# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

words_list = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words_list.append(word)

long_words = []

for w in words_list:
    if len(w) > 20:
        long_words.append(w)

print(long_words)