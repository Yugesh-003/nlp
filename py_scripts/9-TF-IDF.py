from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "I love natural language processing",
    "Natural language processing is a lovely field",
    "I enjoy learning about NLP and machine learning"
]

print(documents)

# Create the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

print(vectorizer)

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

#It print the vocabulary with Score
# print("Vocabulary Dictionary:")
# print(vectorizer.vocabulary_)
# print(tfidf_matrix)

# Converting sparse matrix into dense matrix
dense_matrix = tfidf_matrix.toarray()
print(dense_matrix)

# Get feature names (vocabulary)
feature_names = vectorizer.get_feature_names_out()
print("Count of features",len(feature_names))

for word in feature_names:
    print(word)

# Convert TF-IDF matrix to a dense format and display
for i, doc_vector in enumerate(tfidf_matrix.toarray()):
    print(f"\nDocument {i+1} TF-IDF Scores:")

    for word, score in zip(feature_names, doc_vector):
        if score > 0:
            print(f"{word}: {score:.4f}")
