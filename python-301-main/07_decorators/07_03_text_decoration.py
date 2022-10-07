# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate_with(chr):
    def decorate_func(func):
        def wrapper(msg):
            msg = f"{chr * 20}\n{msg}\n{chr * 20}"
            return func(msg)
        return wrapper
    return decorate_func

@decorate_with("$")
def message(text):
    print(text)

message("money")