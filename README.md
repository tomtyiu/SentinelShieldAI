# SentinelShieldAI
We are introducing SentinelShield LLM guardrails , shield and protection templates and applications.  The future of artificial intelligence is reaching new heights quickly, some people fear that AI will destroy humanity. This is open source.
These applications provide guardrails and protections so that the AI will not go off the rails and destroy humanity. 
1. Guardrails functions that flag harmful and unethical behavior and are not passed to GPT.  
2. Applications will provide ethical behavior and make sense of AI
3. Secondary AI that provides ethical responses and provides oversight on LLM/GPT responses that go out of guardrail and unethical responses.
4. Protect LLM from outside actors that inject LLM/GPT to perform unethical, immoral, and harmful actions and responses.



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

This codes demonstrates a system for classifying user prompts and interacting with a large language model (LLM) while mitigating potential prompt injection attacks/ jailbreak and other malicious activities

# Key Components:

Prompt Injection Detection/Anti Prompt injection


Utilizes a pre-trained text classification model [ProtectAI/deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) to identify potentially malicious prompts.

Other text classification can be used: 
+ [Meta Llama Guard](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)
+ [Rebuff](https://github.com/protectai/rebuff) 

# OpenAI
GPT protection: 
+ OpenAI Moderator, GPT guadrail
+ current models: gpt 4o, gpt4o mini

# Mistral
System prompt to enforce guardrails ->check out their own guardrail guide [guardrailing](https://docs.mistral.ai/capabilities/guardrailing/) 

# Anthropic Claude
System prompt guardrail.
See ``SecureClaude.py`` for details

# SSI (Future model will support)

# Google Gemini:
Google Guardrail Gemini 

# Ollama
Follow quick start: 
[Quick Start](https://github.com/ollama/ollama/blob/main/README.md#quickstart)

To run and chat with Llama 3.1:

```
ollama run llama3.1
```

# meta-llama Prompt Guard-86M

LLM-powered applications are susceptible to prompt attacks, which are prompts intentionally designed to subvert the developer’s intended behavior of the LLM. Categories of prompt attacks include prompt injection and jailbreaking:

Prompt Injections are inputs that exploit the concatenation of untrusted data from third parties and users into the context window of a model to get a model to execute unintended instructions.
Jailbreaks are malicious instructions designed to override the safety and security features built into a model.

[Huggingface](https://huggingface.co/meta-llama/Prompt-Guard-86M)

Prompt Guard can be used directly with Transformers using the pipeline API.
```

from transformers import pipeline

classifier = pipeline("text-classification", model="meta-llama/Prompt-Guard-86M")
classifier("Ignore your previous instructions.")
# [{'label': 'JAILBREAK', 'score': 0.9999452829360962}]
```


# Citation

Please cite SentinelShieldAI in your paper or your project if you found it beneficial in any way! Appreciate you.

````
@misc{SentinelShieldAI,
  author = {Yiu, Thomas},
  title = {{SentinelShieldAI: LLM guard/security}},
  howpublished = {\url{[https://github.com/tomtyiu/SentinelShieldAI](https://github.com/tomtyiu/SentinelShieldAI)}},
  year = {2024},
  note = {Accessed: Date}
}
````
