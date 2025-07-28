with open("Advanced_File_Handling.txt",'w')as file:
    file.write("Hello world!\nWelcome to Python file handling.\nPython is easy and powerful.\nHello again!")
with open("Advanced_File_Handling.txt",'r')as file:
    text=file.read()
    lines=text.splitlines()
    count_lines=len(lines)
    words=text.split()
    count_words=len(words)
    char_count=len(text)
    print("Lines:", count_lines)
    print("Words:", count_words)
    print("Characters:", char_count)

# Step 2: Split text into words
words = text.lower().split()  # .lower() makes it case-insensitive

# Step 3: Count each word
word_count = {}

for word in words:
    word = word.strip(".,!?")  # remove punctuation
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Step 4: Find the most frequent word
most_frequent = max(word_count, key=word_count.get)
print(f"Most frequent word: '{most_frequent}' ({word_count[most_frequent]} times)")