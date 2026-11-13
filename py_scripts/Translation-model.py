from transformers import MarianMTModel, MarianTokenizer

# Load pretrained English-to-French model
model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = MarianTokenizer.from_pretrained(model_name)
    
model = MarianMTModel.from_pretrained(model_name)
# Loads the pretrained translation model

# Input text
text = "Natural Language Processing enables computers to understand human language."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt", padding=True)

print(inputs)


# Generate translation
translated_tokens = model.generate(**inputs, max_length=50)

translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

print("English:", text)
print("French:", translated_text)

