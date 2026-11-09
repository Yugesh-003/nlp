# ------------------------------------------------------------
# ## Bigram with libraries

from collections import defaultdict
import re
import nltk
from nltk.util import bigrams

# Sample corpus
corpus = "I love NLP. NLP and AI is fun. And I love learning new things in NLP."

# Step 1: Preprocessing (lowercasing and tokenization)
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens

print(corpus)
tokens = preprocess(corpus)

print(tokens)

# Step 2: Create bigrams
print(len(tokens))
bigram_list = list(bigrams(tokens))

for bi in bigram_list:
  print(bi)

# Step 3: Count unigrams and bigrams
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

for word in tokens:
    unigram_counts[word] += 1

for w1, w2 in bigram_list:
    bigram_counts[(w1, w2)] += 1


bigram_counts

unigram_counts

# Step 4: Calculate bigram probabilities
bigram_probabilities = {}

for (w1, w2), count in bigram_counts.items():

    bigram_probabilities[(w1, w2)] = count / unigram_counts[w1]

## do we reallyy need to write this just to print???
# Step 5: Display the bigram probabilities
print("Bigram Probabilities:\n")
for (w1, w2), prob in bigram_probabilities.items():
    print(f"P({w2} | {w1}) = {prob}")


# Sample text
text = "I love NLP"

# Tokenize the text
tokens = preprocess(text)
tokens

# Probability calculation using formula
prob = 1

for i in range(len(tokens) - 1):
    pair = (tokens[i], tokens[i+1])
    print(pair)

    if pair in bigram_probabilities:
        prob *= bigram_probabilities[pair]
    else:
        prob = 0
        break

# Output
print("\nProbability of New Sentence:")
print(prob)

