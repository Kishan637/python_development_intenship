# File Manipulation - Word Count Program

import os
import string

filename = "sample.txt"

# Check if file exists
if not os.path.exists(filename):
    print("❌ File not found! Please create 'sample.txt' in the same folder.")
else:
    # Read file
    with open(filename, "r") as file:
        text = file.read().lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Split into words
    words = text.split()

    # Count word frequency
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Display result
    print("\n📊 Word Count Result:\n")

    for word in sorted(word_count):
        print(f"{word} : {word_count[word]}")