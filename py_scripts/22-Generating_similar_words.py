# pip install gensim

from gensim.models import Word2Vec
from nltk.corpus import brown
import nltk

# Download the Brown corpus
# nltk.download('brown')
#  Try to find out the similar words for the following words.... "king" , "queen"

# Load sentences from Brown corpus
sentences = brown.sents()

# print(sentences)

# Train Word2Vec model
# Word2Vec learns a word's meaning from the words that occur around it.
model = Word2Vec(sentences, vector_size=100, window=5, min_count=2, workers=4)

# Find similar words
word = "money"
# Refer the code given below in the next section for more understanding
# print(model.wv.key_to_index)
# check if word exists in vocabulary
if word in model.wv.key_to_index:
    print(f"Words similar to '{word}':")
    # Word similarity and Closeness is measured using cosine similarity between the word vectors.
    similar_words = model.wv.most_similar(word, topn=5)
    # Find out the use of the parameter topn....
    for w, score in similar_words:
        print(f"{w} → {score:.4f}")
else:
    print(f"'{word}' not found in vocabulary!")

# # Find similar words
# word = "king"
# # Refer the code given below in the next section for more understanding
# print(model.wv.key_to_index)
# # check if word exists in vocabulary
# if word in model.wv.key_to_index:
#     print(f"Words similar to '{word}':")
#     # Word similarity and Closeness is measured using cosine similarity between the word vectors.
#     similar_words = model.wv.most_similar(word, topn=5)
#     # Find out the use of the parameter topn....
#     for w, score in similar_words:
#         print(f"{w} → {score:.4f}")
# else:
#     print(f"'{word}' not found in vocabulary!")

# # Find similar words
# word = "queen"
# # Refer the code given below in the next section for more understanding
# print(model.wv.key_to_index)
# # check if word exists in vocabulary
# if word in model.wv.key_to_index:
#     print(f"Words similar to '{word}':")
#     # Word similarity and Closeness is measured using cosine similarity between the word vectors.
#     similar_words = model.wv.most_similar(word, topn=5)
#     # Find out the use of the parameter topn....
#     # for w, score in similar_words:
#     #     print(f"{w} → {score:.4f}")
# else:
#     print(f"'{word}' not found in vocabulary!")

# # Code to illustrate model.wv.key_to_index.

# from gensim.models import Word2Vec
# sentences = [["i", "love", "nlp"], ["nlp", "is", "fun"], ["love", "machine", "learning"]]

# model = Word2Vec(sentences, vector_size=50, window=3, min_count=1, workers=2)

# print(model.wv.key_to_index)

# # Code to illustrate model.wv.key_to_index.
# from gensim.models import Word2Vec
# sentences = [["i", "love", "nlp"], ["nlp", "is", "fun"], ["love", "machine", "learning"]]

# model = Word2Vec(sentences, vector_size=50, window=3, min_count=2, workers=2)

# print(model.wv.key_to_index)
