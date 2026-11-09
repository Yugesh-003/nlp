import nltk

# Download necessary resources (only once)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

#Input
text = "Natural Language Processing enables machines to understand human language."
print(text)
#Tokenize the sentence
tokens = nltk.word_tokenize(text)

#Perform POS tagging
pos_tags = nltk.pos_tag(tokens)

#Print the result
print("Tokens and their POS tags:")
for word, tag in pos_tags:
    print(f"{word:15} -> {tag}")

# #POS Tagger using Hidden Markov Models (HMM) and the Viterbi Algorithm.

# import nltk, re, pprint
# import numpy as np
# import pandas as pd
# import requests
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pprint, time
# import random
# from sklearn.model_selection import train_test_split
# from nltk.tokenize import word_tokenize

# # reading the Treebank tagged sentences
# nltk.download('treebank')
# treeword = list(nltk.corpus.treebank.tagged_sents())

# print(treeword)

# # first few tagged sentences
# print(treeword[:5])

# # Splitting into train and test
# random.seed(1234)
# train_set, test_set = train_test_split(treeword,test_size=0.3)

# print(len(train_set))
# print(len(test_set))
# print(train_set[:5])

# # Getting list of tagged words
# train_tagged_words = [tup for sent in train_set for tup in sent]
# len(train_tagged_words)

# # tokens
# tokens = [pair[0] for pair in train_tagged_words]
# tokens[:10]

# # vocabulary
# V = set(tokens)
# print(len(V))

# # number of tags
# T = set([pair[1] for pair in train_tagged_words])
# len(T)

# print(T)

# import nltk

# # Download necessary resources (only once)
# nltk.download('punkt_tab')
# nltk.download('averaged_perceptron_tagger_eng')


# # Input sentence
# text = "The whole team played well. You are doing well for yourself. Well, this is a lot of work. The well is dry. Tears were beginning to well in her eyes."

# # Step 1: Tokenize the sentence
# tokens = nltk.word_tokenize(text)

# # Step 2: Perform POS tagging
# pos_tags = nltk.pos_tag(tokens)

# # Print the result
# print("Tokens and their POS tags:")
# for word, tag in pos_tags:
#     print(f"{word:15} -> {tag}")

