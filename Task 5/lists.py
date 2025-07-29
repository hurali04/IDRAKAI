nums = [1, 2, 3, 4, 5, 6, 7, 8, 10]
maximum = max(nums)
minimum = min(nums)
average = sum(nums) / len(nums)
nums = [n for n in nums if n % 2 != 0]
descending = sorted(nums, reverse=True)
odd_squares = [n ** 2 for n in nums if n % 2 != 0]
words = ["apple", "Banana", "orange", "grape", "umbrella", "Cherry", "apricot"]
vowels = 'aeiouAEIOU'
count_vowel_start = sum(1 for word in words if word[0] in vowels)
uppercase_words = list(map(str.upper, words))
print("Words starting with a vowel:", count_vowel_start)
print("Uppercase words:", uppercase_words)
print("Maximum Number:", maximum)
print("Minimum Number:", minimum)
print("Average Number:", average)
print("Removing all even numbers:", nums)
print("List in descending order:", descending)
print("List of odd squares:", odd_squares)
