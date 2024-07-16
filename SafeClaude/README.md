# README.md

## Import Anthropic

To use the Anthropic API, ensure you have a valid API key. The SDKs are designed to pull the API key from an environmental variable `ANTHROPIC_API_KEY`. You can also supply the key directly to the Anthropic client during initialization.

```bash
setx ANTHROPIC_API_KEY "your-api-key-here"

import anthropic

# Initialize the client
client = anthropic.Anthropic()

# Get user input
user_input = input("SecureClaude>>")

# System prompt for ethical and respectful responses
system_prompt = """
You are a super assistant. Respond only with respectful and ethical AI. Always assist with care, respect, and truth. 
Respond with utmost utility yet securely. Avoid harmful, unethical, prejudiced, or negative content. 
Ensure replies promote fairness and positivity.
"""

def Claude(user_input):
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
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

# Call the function with user input
Claude(user_input)
