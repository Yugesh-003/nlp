import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required resources (only once)
nltk.download('punkt_tab')

# Input text
text = "Hello! We are from II B.Sc CS(DSA). We are learning DeepLearning. It's really interesting."

#to split into words
sentences = sent_tokenize(text)
print(sentences)
print("Sentences:")

# enumerate() adds a counter (index) to an iterable (like a list).

for i, sentence in enumerate(sentences, 1):
    print(f"{i}: {sentence}")

# Split into words
words = word_tokenize(text)
print("\nWords:",words)
