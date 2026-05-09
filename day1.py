import ollama

response = ollama.chat(
    model="qwen2.5-coder:7b",
    messages=[
        {"role": "user", "content": "Hello, are you working?"}
    ]
)

print(response['message']['content'])