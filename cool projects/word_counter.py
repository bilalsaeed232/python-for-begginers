text = input("Enter a sentence: ")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word counts:")
for word, count in word_count.items():
    print(f"{word}: {count}")