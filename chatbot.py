# Simple Chatbot using Python

# Define responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bunch of code, but thanks for asking! How can I assist you?",
    "what is your name": "I'm a simple Python chatbot created to help you!",
    "bye": "Goodbye! Have a nice day!",
    "help": "I'm here to help! You can ask me questions, say 'hi', or type 'bye' to end the conversation.",
}

# Function to handle user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    # Check if the input matches any predefined response
    for key in responses:
        if key in user_input:
            return responses[key]
    return "I'm sorry, I don't understand that. Can you try rephrasing?"

# Main chatbot loop
print("Chatbot: Hi! I'm your chatbot. Type 'bye' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    else:
        # Get chatbot response
        response = chatbot_response(user_input)
        print("Chatbot:", response)
