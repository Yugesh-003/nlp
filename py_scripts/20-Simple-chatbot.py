import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import random

# Download necessary NLTK data
nltk.download('punkt_tab')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()


# Sample responses
greetings = ['hello', 'hi', 'hey', 'good morning', 'good evening']
responses_greetings = ['Hello!', 'Hi there!', 'Hey!', 'Greetings!']

farewells = ['bye', 'goodbye', 'see you', 'later']
responses_farewells = ['Goodbye!', 'See you later!', 'Bye!', 'Take care!']

questions = {
    'your name': "I'm a simple chatbot.",
    'how are you': "I'm doing fine, thank you!",
    'what can you do': "I can chat with you. Try saying 'hello'!",
    'help': "You can greet me or ask basic questions."
}


# Function to preprocess user input
def preprocess(sentence):
    tokens = word_tokenize(sentence.lower())
    lemmatized = [lemmatizer.lemmatize(word) for word in tokens] # reduces a word to its lemma (the base or dictionary form).
    return lemmatized


# Main chatbot function
def chatbot_response(user_input):
    user_input = user_input.lower()
    tokens = preprocess(user_input)

    # Greeting
    if any(word in tokens for word in greetings):
    # It checks, for each word in greetings, whether that word is in the user's tokenized input (tokens).
        return random.choice(responses_greetings)
        # It randomly selects one item from a non-empty sequence (like a list or tuple).

    # Farewell
    elif any(word in tokens for word in farewells):
        return random.choice(responses_farewells)

    # Check for known questions
    for key in questions:
        if key in user_input:
            return questions[key]   # to get the value from the dictionary questions that belongs to the given key.

    # Default response
    return "I'm not sure I understand. Can you rephrase that?"


# Chat loop
def chat():
    print("Chatbot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():
            print("Chatbot:", random.choice(responses_farewells))
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Start chat
if __name__ == "__main__": # is a standard Python pattern that controls when your script's code should run.
    chat()
