# ------------------------------------------------------------
# # Stemming Algorithms

# Install NLTK if not already installed
# !pip install nltk
# !pip install stemming

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, RegexpStemmer



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
from stemming.lovins import stem
print("Lovins Stemmer")
for word in words:
    print(word, "->", stem(word))

# ------------------------------------------------------------
# ## Regex-Based Stemmer

reg_stemmer=RegexpStemmer('ing$|s$|e$|able$', min=4)
print("RegexpStemmer")
for word in words:
    print(word, "->", reg_stemmer.stem(word))

reg_stemmer.stem('ingeating')

reg_stemmer.stem('eating')
