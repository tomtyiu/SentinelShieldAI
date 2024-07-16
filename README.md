# SentinelShieldAI
We are introducing SentinelShield LLM guardrails , shield and protection templates and applications.  The future of artificial intelligence is reaching new heights quickly, some people fear that AI will destroy humanity.
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

This codes demonstrates a system for classifying user prompts and interacting with a large language model (LLM) while mitigating potential prompt injection attacks.

# Key Components:

Prompt Injection Detection/Anti Prompt injection


Utilizes a pre-trained text classification model [ProtectAI/deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) to identify potentially malicious prompts.

Other text classification can be used: 
+ [Meta Llama Guard](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)
+ [Rebuff](https://github.com/protectai/rebuff) 

# OpenAI
OpenAI uses OpenAI Moderator. 

# Mistral
System prompt to enforce guardrails ->check out their own guardrail guide [guardrailing](https://docs.mistral.ai/capabilities/guardrailing/) 

# Anthropic Claude
System prompt guardrail.
See ``SecureClaude.py`` for details

# SSI (Future model will support)

# Citation

Please cite SentinelShieldAI in your paper or your project if you found it beneficial in any way! Appreciate you.

````
@misc{SentinelShieldAI,
  author = {Yiu, Thomas},
  title = {{SentinelShieldAI: LLM guard/security}},
  howpublished = {\url{[https://github.com/kyegomez/swarms](https://github.com/tomtyiu/SentinelShieldAI)}},
  year = {2024},
  note = {Accessed: Date}
}
````
