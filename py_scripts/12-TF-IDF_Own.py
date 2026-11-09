import math

texts = [
    "I love natural language processing",
    "Natural language processing is interesting",
    "I love machine learning"
]

# Split sentences into words
word_docs = [text.lower().split() for text in texts]

# Build unique word list
words = []

for sentence in word_docs:
    for item in sentence:
        if item not in words:
            words.append(item)

# Calculate TF-IDF scores
for index, sentence in enumerate(word_docs):

    print("\nDocument", index + 1)

    for term in words:

        # Term Frequency
        tf = sentence.count(term) / len(sentence)

        # Document Frequency
        doc_freq = 0
        for other in word_docs:
            if term in other:
                doc_freq += 1

        # Inverse Document Frequency
        idf = math.log(len(word_docs) / doc_freq)

        # TF-IDF score
        score = tf * idf

        if tf != 0:
            print(f"{term}: TF={tf:.3f}, IDF={idf:.3f}, TF-IDF={score:.3f}")