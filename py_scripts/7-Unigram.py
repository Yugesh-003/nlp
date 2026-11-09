import re
from collections import Counter

# Sample training text
text = """
Machine learning helps computers learn from data.
"""

# Step 1: Tokenize (convert to lowercase and extract words)
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# Step 2: Build Unigram Model (count word frequencies)
def build_unigram_model(text):
    tokens = tokenize(text)
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
