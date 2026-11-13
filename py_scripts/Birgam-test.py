import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')

text = "I love NLP. NLP and AI is fun and I love learning new things in NLP."

# Tokenization
words = word_tokenize(text.lower())

# Generate Bigrams and Unigrams
bigrams = list(ngrams(words, 2))
unigrams = Counter(words)
frequency = Counter(bigrams)

# Calculate Bigram Probability
print("Bigram Probabilities:")

for (w1, w2), count in frequency.items():
    probability = count / unigrams[w1]
    print(f"P({w2} | {w1}) = {probability}")

# Probability of a new sentence
sentence = "I love NLP"
new_words = word_tokenize(sentence.lower())
new_bigrams = list(ngrams(new_words, 2))

prob = 1

for w1, w2 in new_bigrams:
    prob *= frequency[(w1, w2)] / unigrams[w1]

print("\nProbability of New Sentence:")
print(prob)