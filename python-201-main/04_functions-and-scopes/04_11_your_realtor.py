# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_ad(**kwargs):
    description = 'This beautiful property has the following great features:'
    print(description)
    for k, v in kwargs.items():
        print(f'-{k}: {v}')

real_ad(Area = '2000 sqft', Bedrooms = 2, Bathrooms = 1.5) 
    