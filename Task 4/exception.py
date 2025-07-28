def division(a, b):
    try:
        result = a / b
    except ValueError:
        print("Enter a correct value")
    except ZeroDivisionError:
        print("Infinity (division by zero)")
    else:
        print("Result will be:", result)
    finally:
        print("Result displayed successfully\n")


def file_reading(filename):
    try:
        with open(f"{filename}.txt", 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("File not found")
    else:
        print("File content:\n", content)
    finally:
        print("File operation over\n")


def key_lookup(dictionary, key):
    try:
        print("Value:", dictionary[key])
    except KeyError:
        print("Key not found")
    finally:
        print("Dictionary operation over\n")

division(10, 0)
file_reading("Logging_Time")  
key_lookup({"name": "Ali", "age": 22}, "name")
