# PROJECT: HTML Element Decorator

# Write a decorator function that wraps text passed to it in a specified HTML tag. 
# The user should be able to decide which tag to use.

def tagify(tag):
    def initial_func(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"
            #returns the return value of the function, not the arguments
        return wrapper
    return initial_func

@tagify("p")
def greet(name):
    return f"Hello, {name}"

@tagify("div")
def lorem():
    return "Lorem borem jorem..."

print(greet("John"))
print(lorem())