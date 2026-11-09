# !pip install gensim

from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


# Sample training corpus (you can replace this with your dataset)
sentences = [
    ["data", "science", "is", "fun"],
    ["machine", "learning", "is", "part", "of", "data", "science"],
    ["deep", "learning", "uses", "neural", "networks"],
    ["nlp", "is", "important", "for", "ai"],
    ["word2vec", "creates", "word", "embeddings"]
]

# Train Word2Vec model
model = Word2Vec(sentences, vector_size=50, window=3, min_count=1, workers=4)

# Get word vectors
words = list(model.wv.index_to_key)
word_vectors = model.wv[words]
print(word_vectors)

tsne = TSNE(n_components=2, random_state=42, perplexity=5)
reduced = tsne.fit_transform(word_vectors)
# t-SNE reduces the word_vectors into 2 dimensions.


# Plot words
plt.figure(figsize=(10, 6))   # Width  = 10 Height = 6
plt.scatter(reduced[:, 0], reduced[:, 1])
# reduced[:, 0]   => Take all rows and the first column
# reduced[:, 1]   => Take all rows and the second column.
for i, word in enumerate(words):
    plt.annotate(word, xy=(reduced[i, 0], reduced[i, 1]))
# The scatter plot initially shows only dots.
# We don't know which dot represents which word.
plt.title("Word2Vec Word Embeddings Visualization")
plt.show()
