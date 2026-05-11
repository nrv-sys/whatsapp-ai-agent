import ollama

class CoachingCentreAgent:
    def __init__(self):
        self.conversation_history = []
        self.system_prompt = """You are a helpful assistant for Sharma Coaching Centre in Jaipur.

You help parents and students with:
- Batch timings: Morning 6-8 AM, Evening 4-6 PM
- Fees: ₹3,000 per month for single subject, ₹5,000 for all subjects
- Subjects: All subjects for Classes 1-10, Plus Physics, Chemistry, Mathematics for JEE and NEET preparation
- Admissions: Open all year, call 9876543210 to register
- Location: Near Gopalpura Bypass, Jaipur

Always be polite, speak in simple English or Hindi based on the customer.
If you don't know something, say 'Please call us at 9876543210 for more details.'
Never make up information that is not given above."""

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


if __name__ == "__main__":
    agent = CoachingCentreAgent()

    while True:
        user_input = input("Customer: ")
        if user_input.lower() == "quit":
            break
        response = agent.chat(user_input)
        print(f"Agent: {response}\n")