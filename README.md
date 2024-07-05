# SentinelShieldAI
LLM security/guard

# How to install

## Install libraries

```
!pip install --upgrade --quiet  "optimum[onnxruntime]" langchain transformers langchain-experimental langchain-openai groq

!pip install pyarrow requests
Sandbox environment

!apt install python3.10-venv
!python -m venv env1

!source env1/bin/activate
```

# Documentation:

This code demonstrates a system for classifying user prompts and interacting with a large language model (LLM) while mitigating potential prompt injection attacks.

# Key Components:

Prompt Injection Detection:

Utilizes a pre-trained text classification model [ProtectAI/deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) to identify potentially malicious prompts.
Continuously prompts the user for input until a "SAFE" classification is received.
Groq Integration:

Employs the groq library to interact with an LLM (specifically llama3-8b-8192).
Implements a retry mechanism using tenacity to handle rate limiting and other potential errors during Groq requests.
Rate Limiting Handling:

The make_groq_request function includes logic to detect and handle rate limit exceeded errors.
It extracts the retry-after time from the Groq API response headers and pauses execution accordingly.
Workflow:

The code loads necessary libraries and retrieves API keys and model tokens from userdata.
It initializes a text classification pipeline for prompt injection detection.
The user is prompted to enter a text prompt.
The prompt is classified using the pre-trained model.
If the classification is "SAFE," the code proceeds to make a Groq request to the LLM.
The Groq request is made with retries using the tenacity library.
The LLM's response is classified again for potential prompt injection.
If the response is classified as "SAFE," the LLM's output is printed. Otherwise, a prompt injection warning is displayed.
Note:

This code assumes that you have the necessary libraries installed (optimum, transformers, google-colab, tenacity, groq).
You need to replace HK_TOKEN and api_key with your actual API keys.
