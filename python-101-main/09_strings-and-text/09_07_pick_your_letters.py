# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
we = word[1:3]
s = word[7:6:-1]
ee = word[2:4]
t = word[0:1]
r = word[6:7]

print(we + " " + s + ee + " " + t + r + ee + s)

print(word[1:3] + " " + word[7:6:-1] + word[2:4] + " " + word[0:1] + word[6:7] + word[2:4] + word[7:6:-1])