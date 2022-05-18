# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.

words_list = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words_list.append(word)

words_list.reverse()

with open("word_reverse.txt", "w") as fout:
    for w in words_list:
        fout.write(w)
        fout.write("\n")