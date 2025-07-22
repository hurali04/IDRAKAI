def longest_string(strings):
    for s in strings:
        if len(s) > len(strings):
            strings= s
    return strings
words = ["apple", "banana", "watermelon", "kiwi","blueberry","strawberry"]
result = longest_string(words)
print("Longest string is:", result)
