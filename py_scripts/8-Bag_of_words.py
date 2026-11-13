from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "I love machine learning",
    "Machine learning is fun",
    "I love learning new things"
]

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the documents
cv = vectorizer.fit_transform(documents)
# print(X)
# # Change it into dense matrix and display the answer.
print(vectorizer.vocabulary_)

# Get the feature (word) names
feature_names = vectorizer.get_feature_names_out()

# Convert the result to array
bow_matrix = cv.toarray()

# Display results
print("Vocabulary / Features:")
print(feature_names)

print("\nBag of Words Matrix:")
for i, row in enumerate(bow_matrix):
    print(f"Document {i+1}: {row}")
