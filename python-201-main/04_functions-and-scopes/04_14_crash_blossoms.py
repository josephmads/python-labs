# A CLI program that blossomizes sentences.

# function to capitalize each word.
def titlecase(text):
    titlecase = []
    for word in text.split():
        cap_word = word.capitalize()
        titlecase.append(cap_word)
    return " ".join(titlecase)

# collect intial user input
user_input = input("Enter your sentence (type 'exit' to quit): ")

while user_input.lower() != "exit":
    crash_blossom = titlecase(user_input)
    print(crash_blossom)
    # collect user input
    user_input = input("Enter your sentence (type 'exit' to quit): ")
    