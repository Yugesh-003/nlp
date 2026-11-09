import re
from collections import Counter

# Sample text
text = """
Data science uses data to solve problems."""

# Convert text to lowercase and tokenize (split into words)
tokens = re.findall(r'\b\w+\b', text.lower())
#  \w matches any word character: [A-Za-z0-9_]
# \b represents Word boundary
print(tokens)

# Count total number of words (tokens)
total_tokens = len(tokens)

# Count number of unique words (types)
unique_tokens = len(set(tokens))

# Count occurrences of the word "data"
word_the_count = tokens.count('data')

# Calculate percentage of "the" in all tokens
percentage_the = (word_the_count / total_tokens) * 100

# Print results
print("a) Total number of words (tokens):", total_tokens)
print("b) Number of different words (types):", unique_tokens)
print("c) Occurrences of the word 'data':", word_the_count)
print("d) Percentage of 'data': {:.2f}%".format(percentage_the))
