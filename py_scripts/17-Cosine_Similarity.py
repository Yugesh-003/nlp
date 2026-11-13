import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Natural Language Processing makes computers understand human language",
    "Deep Learning is used in Natural Language Processing",
    "I love playing football in the evening"
]

# TF-IDF representation
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

# Plot heatmap
plt.figure(figsize=(6,5))
sns.heatmap(cosine_sim, annot=True, xticklabels=["Doc1","Doc2","Doc3"], yticklabels=["Doc1","Doc2","Doc3"])
plt.title("Cosine Similarity Heatmap")
plt.show()
