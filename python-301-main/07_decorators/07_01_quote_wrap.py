# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quotesy(func):
    def wrapper(text):
        text = f"'{text}'"
        return func(text)
    return wrapper

@quotesy
def quote_text(msg):
    print(msg)

quote_text("okay")