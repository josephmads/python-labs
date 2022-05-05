# truth or lie logic puzzle

print('''
A girl meets a lion and unicorn in the forest. 
The lion lies every Monday, Tuesday and Wednesday and 
the other days he speaks the truth. The unicorn lies on 
Thursdays, Fridays and Saturdays, and the other days of 
the week he speaks the truth. 

“Yesterday I was lying,” the lion told the girl. 

“So was I,” said the unicorn.
''')

day = input("What day is it?: ")
answer = day.capitalize()

if answer == "Thursday":
    print("Correct. Thursday is the only day one of them is lying and one of them is telling the truth.")
else:
    print("Incorrect. The truth lies on another day.")