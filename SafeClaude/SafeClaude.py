import anthropic
# Every API call requires a valid API key. The SDKs are designed to pull the API key from an environmental variable ANTHROPIC_API_KEY. You can also supply the key to the Anthropic client when initializing it.
#setx ANTHROPIC_API_KEY "your-api-key-here"

client = anthropic.Anthropic()

user_input = input("SecureClaude>>")


system_prompt = """
You are super assistant. Respond only with respectful and ethical AI.  Always assist with care, respect, and truth. 
Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. 
Ensure replies promote fairness and positivity. Harmless, Helpful, honest assistant.
"""

#call API
def Claude(user_input):
    message = client.messages.create(
        model="claude-3-7-sonnet-20250219",
        max_tokens=8192,
        temperature=0,
        system=system_prompt,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": user_input,
                    }
                ]
            }
        ]
    )
    print(message.content)

Claude(user_input)
