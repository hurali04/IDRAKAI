import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The time to execute the function {func.__name__} is {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling Function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Resulting value is: {result}")
        return result
    return wrapper

@logging
@execution_time
def multiply(a, b):
    return a * b

multiply(10, 50)
