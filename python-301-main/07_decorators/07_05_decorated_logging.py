# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

from datetime import datetime


def time_stamp(func):
    def wrapper(msg):
        dt1 = datetime.now()
        # print(f"Started Execution at: {dt1}")
        result = func(msg)
        dt2 = datetime.now()
        print(f"Execution time: {dt2-dt1}")
        return result
    return wrapper

@time_stamp
def message(text):
    print(text)


message("Is it working?")