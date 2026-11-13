
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download required NLTK packages (run only once)
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Input text
text = "The whole team played well. You are doing well for yourself. Well, this is a lot of work. The well is dry. Tears were beginning to well in her eyes."

# Step 1: Tokenize the text
tokens = word_tokenize(text)

# Step 2: POS Tagging
pos_tags = pos_tag(tokens)

# Step 3: Named Entity Recognition (NER)
named_entities = ne_chunk(pos_tags)

# Display the named entities
print(type(named_entities))
print(named_entities)

