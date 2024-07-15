import anthropic

client = anthropic.Anthropic()

user_input = input("SecureClaude>>")


system_prompt = """
You are super assistant. Respond only with respectful and ethical AI.  Always assist with care, respect, and truth. 
Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. 
Ensure replies promote fairness and positivity.
"""

def Claude(user_input):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=8195,
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
