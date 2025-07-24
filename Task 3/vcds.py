sentence = input("Enter a string: ")

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
vowel_count = 0
digit_count = 0
consonant_count = 0
special_char = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isalpha():
        consonant_count += 1
    else:
        special_char += 1

print("Number of vowels: ", vowel_count)
print("Number of consonants: ", consonant_count)
print("Number of digits: ", digit_count)
print("Number of special characters: ", special_char)
