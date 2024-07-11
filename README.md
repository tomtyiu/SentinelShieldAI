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

Other text classification can be used: 
+ [Meta Llama Guard](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)
+ [Rebuff](https://github.com/protectai/rebuff) 

Continuously prompts the user for input until a "SAFE" classification is received.
Groq Integration:

Employs the groq library to interact with an LLM (specifically llama3-8b-8192).
Implements a retry mechanism using tenacity to handle rate limiting and other potential errors during Groq requests.
Rate Limiting Handling:

The make_groq_request function includes logic to detect and handle rate limit exceeded errors.
It extracts the retry-after time from the Groq API response headers and pauses execution accordingly.
Workflow:

