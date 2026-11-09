import nltk
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize

# Download NLTK resources
nltk.download('punkt_tab')

# Sample text
text = """
Natural Language Processing (NLP) is a field of Artificial Intelligence that focuses on the interaction
between computers and humans using natural language. The ultimate goal of NLP is to enable computers
to understand, interpret, and generate human languages in a way that is both valuable and meaningful.
Applications of NLP are everywhere because people communicate almost everything in language:
search engines, chatbots, translation services, sentiment analysis, and speech recognition systems.
"""

# Step 1: Split text into sentences
sentences = sent_tokenize(text)

# Step 2: Convert sentences to TF-IDF vectors
vectorizer = TfidfVectorizer()
sentence_vectors = vectorizer.fit_transform(sentences)

# Step 3: Compute similarity matrix
similarity_matrix = cosine_similarity(sentence_vectors)

# Step 4: Build graph and apply PageRank
nx_graph = nx.from_numpy_array(similarity_matrix)

scores = nx.pagerank(nx_graph)  # Used by Google to rank web pages

print("Scores of Page Rank algorithm")
print(scores)

# Step 5: Rank sentences and select top ones
ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
print("Ranked Sentences")
print(ranked_sentences)
print("\n")
print(ranked_sentences[0][1])
print("\n")
print(ranked_sentences[1][1])
print("\n")
print(ranked_sentences[2][1])
print("\n")

# Step 6: Generate summary (top 2 sentences)
summary = " ".join([ranked_sentences[i][1] for i in range(2)])

summary

