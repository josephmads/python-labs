# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

bad_words = ["oot", "arn", "ang", "eck"]

def censor(func):
    def wrapper(msg):
        for word in bad_words:
            if word in msg:
                new_msg = msg.replace(word, "***")
            else:
                pass
        return func(new_msg)
    return wrapper

@censor
def message(text):
    print(text)

message("This ding dang thing won't work!")
message("Shoot! I missed.")