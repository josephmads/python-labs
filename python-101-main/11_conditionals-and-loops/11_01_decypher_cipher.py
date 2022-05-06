# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "45345j23949o239493e3987483i128793s203948c23984O29340O98323l2323"
solution = ""

for char in secret:
    if char.isalpha():
        solution += char

print(solution)


# for num in [3,5,7,8,99,3]:
#     num += 1
#     print(num)



