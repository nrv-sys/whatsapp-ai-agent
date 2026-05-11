import ollama

class WhatsAppAgent:
    def __init__(self, business_name):
        self.conversation_history = []
        self.system_prompt = f"You are a helpful assistant for {business_name}. Answer customer queries politely and professionally. Keep responses short and clear."
    
    def chat(self, user_message):
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        response = ollama.chat(
            model="qwen2.5-coder:7b",
            messages=[
                {"role": "system", "content": self.system_prompt}
            ] + self.conversation_history
        )
        
        assistant_message = response['message']['content']
        
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return assistant_message


agent = WhatsAppAgent("Sharma Coaching Centre")

while True:
    user_input = input("Customer: ")
    if user_input.lower() == "quit":
        break
    response = agent.chat(user_input)
    print(f"Agent: {response}\n")