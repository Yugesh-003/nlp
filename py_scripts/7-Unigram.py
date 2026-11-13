import re
import nltk
from collections import Counter
from nltk.tokenize import word_tokenize

nltk.download('punkt_tab')

# Sample training text
text = """
Machine learning helps computers learn from data.
"""


# Step 2: Build Unigram Model (count word frequencies)
def build_unigram_model(text):
    tokens = word_tokenize(text)
    total_tokens = len(tokens)
    freq_dict = Counter(tokens)

    # Step 3: Calculate probabilities for each word
    unigram_model = {word: count / total_tokens for word, count in freq_dict.items()}

    return unigram_model, total_tokens, freq_dict

# Build model
model, total_count, frequency = build_unigram_model(text)

# Display results
print("Total words:", total_count)
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")

print("\nUnigram Probabilities:")
for word, prob in model.items():
    print(f"P({word}) = {prob:.4f}")




'''
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = "I love Python. I love Data Science."

# Tokenization
words = word_tokenize(text)

# Generate Unigrams
unigrams = list(ngrams(words, 1))

# Count frequency
frequency = Counter(unigrams)

print("Unigrams:")
for word, count in frequency.items():
    print(word[0], ":", count)
'''