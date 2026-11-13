#Synset = Synonym Set. It is a group of words (lemmas) that share the same meaning in a specific context.
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

synsets = wn.synsets('actor')  # Get the input from user and apply
# print(wn.synsets("bank"))

for syn in synsets:
    print(f"Synset: {syn.name()}")
    print(f"  Lemmas: {[l.name() for l in syn.lemmas()]}")
    print(f"  Definition: {syn.definition()}")
    print(f"  Examples: {syn.examples()}")

syns = wn.synsets("bank")

print(syns[:3])

