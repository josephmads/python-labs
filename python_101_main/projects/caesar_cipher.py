# replicate the caesar cypher.

secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
alpha = "abcdefghijklmnopqrstuvwxyz"
index = ""
encryption = ""


for char in secret.lower():
    if char in alpha:
        index = (alpha.find(char) + cipher) % len(alpha)
        encryption += alpha[index]
    else:
        encryption += char
        

print(encryption)    

