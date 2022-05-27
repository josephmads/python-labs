# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

my_name = 'Joe Madsen'

# function 1 - goofy name generator
def goof_name(name):
    parts = name.split(' ')
    parts1 = parts[1]
    first_name = parts[0] + parts1[-3:]
    last_name_goof = reverser(parts1[:3]) * 3
    last_name = last_name_goof.capitalize()
    return f'{first_name} {last_name}'

# function 2 - string reverser
def reverser(rev):
    return rev[::-1]

# function 3 - goofy essay converter
def goof_essay(text, by_line):
    text_list = text.split(' ')
    goof_list = []
    for word in text_list:
        if len(word) > 5:
            goof_list.append((reverser(word) + 'oogy'))
        else:
            goof_list.append(word)
    new_text = ' '.join(goof_list)
    return f'{new_text}!\nby, {goof_name(by_line)}'

print(goof_essay(input('Write a short essay: '), input('Enter your name: ')))
    