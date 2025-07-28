import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time of '{func.__name__}': {end_time - start_time:.4f} seconds")
        return result
    return wrapper
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper
@log_calls
@execution_time
def multiply(a, b):
    time.sleep(1)  # simulate delay
    return a * b

multiply(5, 10)
