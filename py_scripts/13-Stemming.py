# ------------------------------------------------------------
# # Stemming Algorithms

# Install NLTK if not already installed
# !pip install nltk

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer
import re

words = ["eating","eats","eaten","writing","writes","programming"]

# ------------------------------------------------------------
# ## Porter Stemmer

ps = PorterStemmer()
print("PorterStemmer")
for word in words:
    print(word, "->", ps.stem(word))

# ------------------------------------------------------------
# ##  Lancaster Stemmer or the Paice-Husk Stemmer

ls = LancasterStemmer()
print("LancasterStemmer")
for word in words:
    print(word, "->", ls.stem(word))

# ------------------------------------------------------------
# ## Snowball Stemmer

ss = SnowballStemmer("english")
print("SnowballStemmer")
for word in words:
    print(word, "->", ss.stem(word))

# ------------------------------------------------------------
# ## Lovins Stemmer (Simplified)

# !pip install stemming

# print(words)
print("Lovins Stemmer")
from stemming.lovins import stem
for word in words:
    print(stem(word))

# ------------------------------------------------------------
# ## Regex-Based Stemmer

from nltk.stem import RegexpStemmer
reg_stemmer=RegexpStemmer('ing$|s$|e$|able$', min=4)
print("RegexpStemmer")
for word in words:
    print(word, "->", reg_stemmer.stem(word))

reg_stemmer.stem('ingeating')

reg_stemmer.stem('eating')
