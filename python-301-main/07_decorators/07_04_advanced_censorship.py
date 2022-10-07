# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".


def bad_words(*args):
    def censor(func):
        def wrapper(msg):
            for word in args:
                if word in msg:
                    msg = msg.replace(word[1::], "***")
                else:
                    pass
            return func(msg)
        return wrapper
    return censor

@bad_words("dang", "shoot", "heck")
def message(text):
    print(text)

message("This ding dang thing won't work!")
message("What the heck!")