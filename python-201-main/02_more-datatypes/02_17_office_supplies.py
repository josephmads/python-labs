# Using f-strings, print out the name, last name, and favorite
# office supply item of each person in the given dictionary,
# formatted like so:
#
# LASTNAME, Name           Office supply item
# LONGERLASTNAME, Name     Office supply item

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

for key, val in enumerate(office):
    full_name = val["full_name"].split(" ")
    last_name = full_name[1].upper()
    first_name = full_name[0]
    final_name = f'{last_name}, {first_name}'
    item = val["item"]
    
    print(f'{final_name:<20} {item:>20}')

# for d in office:
#     fav_item = ""
#     last_name = ""
#     first_name = ""
#     for k, v in d:
#         print(v)
#         if k == "full_name":
#             rev_names = v
#             rev_names = rev_names.split(" ")
#             last_name = rev_names[1]
#             first_name = rev_names[0]
            
#         if k == "item":
#             fav_item = v
#         if last_name and first_name and fav_item:
#             print(f'{last_name}, {first_name} {fav_item}')


