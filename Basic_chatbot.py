# Function to greet the user
def greet_user():
    print("ChatBot: Hello! I am your friendly chatbot.")
    print("ChatBot: How can I help you today?")

# Function to handle responses with logic
def get_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there!"
    elif "hi" in user_input or "hey" in user_input or "good morning" in user_input:
        return "Hello! How can I help you?"
    elif user_input == "how are you":
        return "I'm good, thanks for asking!"
    elif "weather" in user_input:
        return "It is really sunny outside!☀️"
    elif "joke" in user_input:
        return "Why did the math book look sad? Because it had too many problems! 😄"
    elif "hungry" in user_input or "food" in user_input:
        return "Maybe grab a snack! How about some dosa, pizza, or fruits? 🍕🍌"
    elif user_input == "what is your name":
        return "I'm ChatBot, your simple assistant."
    elif "help" in user_input or "what can you do" in user_input:
        return "I'm ready to help you. I can chat with you, tell jokes, suggest food, or just keep you company!"
    elif "sad" in user_input:
        return "I'm sorry to hear that. I'm here to cheer you up! 😊"
    elif "happy" in user_input:
        return "That's great to hear! Keep smiling! 😄"
    elif "bored" in user_input:
        return "Let's talk! Or maybe try drawing, music, or watching something fun!"
    elif "thank" in user_input:
        return "You're welcome!"
    elif "do you like me" in user_input:
        return "Of course! I enjoy chatting with you. 😊"
    elif "favourite color" in user_input or "favorite color" in user_input:
        return "I like blue! It reminds me of the calm sky and ocean. What's yours?"
    elif user_input == "bye":
        return "Good bye! Have a great day!"
    elif "fact" in user_input:
        return "Did you know? Your nose can remember 50,000 different scents!👃🧠"
    else:
        return "Sorry, I didn't understand that. Try saying 'tell me a joke' or 'I'm bored'."

# Main chatbot function
def chatbot():
    greet_user()
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("ChatBot:", response)

        if user_input.lower() == "bye":
            break

# Start the chatbot
chatbot()
