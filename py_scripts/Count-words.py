import re
from collections import Counter
from nltk.tokenize import word_tokenize
# Sample text
text = """
Data science uses data to solve problems."""

# Convert text to lowercase and tokenize (split into words)
tokens = word_tokenize(text.lower())
#  \w matches any word character: [A-Za-z0-9_]
# \b represents Word boundary

total_tokens = len(tokens)
unique_tokens = len(set(tokens))
word_counts = Counter(tokens)

print(f"All tokens: {tokens}\n")
print(f"Total words (tokens): {total_tokens}")
print(f"Unique words (types): {unique_tokens}\n")

# print(f"{'Word':<15} {'Count':>6} {'Percentage':>12}")
# print("-" * 35)

for word, count in word_counts.items():
    percentage = (count / total_tokens) * 100
    print(f"Word : {word}") 
    print(f"Count : {count}") 
    print(f"Percentage : {percentage}%")
    print("================================")
