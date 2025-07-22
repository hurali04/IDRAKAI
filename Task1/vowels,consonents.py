sentence = input("Enter a sentence: ")
vowel_set = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
digit_set = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
vowel = 0
consonant = 0
digit = 0
sc = 0
for char in sentence:
    if char in vowel_set:
        vowel += 1
    elif char.isalpha():
        consonant += 1
    elif char in digit_set:
        digit += 1
    elif not char.isspace():
        sc += 1
print("Vowels:", vowel)
print("Consonants:", consonant)
print("Digits:", digit)
print("Special Characters:", sc)
