# ------------------------------------------------------------
# # Sentiment Classifier using Naïve Bayes

# Step 1: Import libraries
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


# Step 2: Sample dataset (positive and negative reviews)
documents = [
    "I love this movie, it was fantastic!",
    "This was the best film I have ever watched",
    "Absolutely wonderful acting and story",
    "I hated this movie, it was terrible",
    "Worst movie ever, such a waste of time",
    "I will never recommend this boring film",
    "The plot was amazing and the characters were great",
    "Awful experience, the acting was so bad",
    "Brilliant direction and fantastic music",
    "Disgusting movie, I walked out of the theater"
]


# Labels: 1 = Positive, 0 = Negative
labels = [1, 1, 1, 0, 0, 0, 1, 0, 1, 0]

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.3, random_state=42)


# Step 4: Convert text to numerical features (Bag of Words)
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)


# Step 5: Train Naïve Bayes classifier
model = MultinomialNB()
model.fit(X_train_counts, y_train)


# Step 6: Make predictions
y_pred = model.predict(X_test_counts)

# Step 7: Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n",
      classification_report(y_test, y_pred))

# Step 8: Test with custom inputs
new_reviews = [
    "I really enjoyed this amazing movie",
    "The film was dull and disappointing"
]

new_counts = vectorizer.transform(new_reviews)
predictions = model.predict(new_counts)

for review, sentiment in zip(new_reviews, predictions):
    print(f"""Review: '{review}' -->
    Sentiment: {'Positive' if sentiment == 1 else 'Negative'}""")
