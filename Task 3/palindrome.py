word = input("Enter a word: ")
if word == ''.join(reversed(word)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
