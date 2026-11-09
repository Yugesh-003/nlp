#Import Libraries
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

#Using Library
ls=WordNetLemmatizer()

#Sample Words
words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

#Print Words
for word in words:
    print(word+"---->"+ls.lemmatize(word,pos='v'))

# v -> verb
ls.lemmatize("goes",pos='v')

# n -> noun
ls.lemmatize("goes",pos='n')

# a -> adjective
ls.lemmatize("goes",pos='a')

# r ->adverb
ls.lemmatize("goes",pos='r')
