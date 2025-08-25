sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = []

for word in words:
    reversed_word = ''
    for char in word:
        reversed_word = char + reversed_word 
    reversed_words.append(reversed_word)

result = ' '.join(reversed_words)
print(f"Result: {result}")
