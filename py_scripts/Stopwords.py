import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Download required resources
nltk.download('punkt_tab')
nltk.download('stopwords')

#Input text
text = "Natural Language Processing helps to get advance knowledge in developing AI models."

#Tokenize text into words
words = word_tokenize(text)

#Load English stopwords
stop_words = set(stopwords.words('english'))

#Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

#Output the filtered words
print("Original text:")
print(text)
print("\nText after removing stopwords:")
print(" ".join(filtered_words))

#Example sentences
examples = [
    "The students from CS(DSA) are so vibrant.",
    "The weather today is very sunny and pleasant.",
    "We are learning Natural Language Processing using Python.",
    "Naresh is not only intelligent but also hardworking.",
    "Can you help me with this task?"
]

#Process each sentence
for i, text in enumerate(examples, 1):
    # Tokenize and remove stopwords
    words = word_tokenize(text)
    filtered = [word for word in words if word.lower() not in stop_words]

#display result
print(f"\nExample {i}:")
print("Original:", text)
print("Without Stopwords:", " ".join(filtered))
