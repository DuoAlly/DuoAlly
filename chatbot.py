from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load a pre-trained language model and tokenizer
model_name = "microsoft/DialoGPT-small"  # You can also use 'gpt2' or another conversational model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Chatbot conversation function
def chat_with_model(input_text, chat_history_ids=None):
    # Encode user input and generate a response
    new_input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")

    # Append new user input to the chat history and generate response
    bot_output = model.generate(
        torch.cat([chat_history_ids, new_input_ids], dim=-1) if chat_history_ids is not None else new_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )

    # Decode and print the response
    response = tokenizer.decode(bot_output[:, chat_history_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, bot_output

# Main loop for the chatbot
print("Chatbot: Hi! I'm a chatbot powered by a language model. Type 'exit' to end the conversation.")
chat_history_ids = None
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a nice day!")
        break
    else:
        response, chat_history_ids = chat_with_model(user_input, chat_history_ids)
        print("Chatbot:", response)
