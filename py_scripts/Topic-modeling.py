# !pip install gensim
# open-source Python library primarily used in Natural Language Processing (NLP) for unsupervised topic modeling and document similarity analysis

import string
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')  # Open Multilingual Wordnet. Used for lemmatization
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# Creating example documents
corpus = ["NLP is an artificial intelligence technology that allows computers to understand, interpret, and generate human language, enabling applications like voice assistants, email spam filters, and machine translation.",
          "Machine learning has the potential to quickly identify trends and patterns in large amounts of data that would be time consuming for humans. These insights can equip businesses, researchers, and society as a whole with new knowledge that has the potential to help them achieve their overall goals.",
          "AI is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy."]

# # Create corpus
# corpus = [doc_1, doc_2, doc_3]


# remove stopwords, punctuation, and normalize the corpus
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
# print(exclude)


def clean(doc):
    stop_free = " ".join(i for i in doc.lower().split() if i not in stop)
    punc_free = "".join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

clean_corpus = [clean(doc).split() for doc in corpus]
print("cleaned corpora :", clean_corpus)

from gensim import corpora

# Creating document-term matrix
dictionary = corpora.Dictionary(clean_corpus)  # a mapping between words and their integer ids
doc_term_matrix = [dictionary.doc2bow(doc) for doc in clean_corpus]
# doc2bow -  the number of occurrences of each distinct word,
# convert the word to its integer word id and
# then the result is returned as a sparse vector
# print(doc_term_matrix)

from gensim.models import LdaModel

# LDA model
lda = LdaModel(doc_term_matrix, num_topics=3, id2word = dictionary)
# num_topics - specifies the desired number of latent topics that
# the LDA model should extract from the doc_term_matrix
# id2word - a mapping between numerical word IDs (as used in the doc_term_matrix)
# and their corresponding actual word strings

# Results
print(lda.print_topics(num_topics=3, num_words=3))

