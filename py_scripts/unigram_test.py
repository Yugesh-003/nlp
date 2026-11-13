import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = "Machine learning helps computers learn from data."

# Tokenization
words = word_tokenize(text)

# Count word frequencies
frequency = Counter(words)

print("Word Frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

# Calculate Unigram Probabilities
total = len(words)

print("\nUnigram Probabilities:")
for word, count in frequency.items():
    probability = count / total
    print(f"P({word}) = {probability:.4f}")