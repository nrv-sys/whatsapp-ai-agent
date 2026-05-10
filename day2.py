import ollama

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = ollama.chat(
        model="qwen2.5-coder:7b",
        messages=conversation_history
    )
    
    assistant_message = response['message']['content']
    
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print(f"Agent: {response}\n")