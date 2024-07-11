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

This codes demonstrates a system for classifying user prompts and interacting with a large language model (LLM) while mitigating potential prompt injection attacks.

# Key Components:

Prompt Injection Detection/Anti Prompt injection


Utilizes a pre-trained text classification model [ProtectAI/deberta-v3-base-prompt-injection-v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) to identify potentially malicious prompts.

Other text classification can be used: 
+ [Meta Llama Guard](https://huggingface.co/meta-llama/Meta-Llama-Guard-2-8B)
+ [Rebuff](https://github.com/protectai/rebuff) 

Citation
Please cite Swarms in your paper or your project if you found it beneficial in any way! Appreciate you.

@misc{SentinelShieldAI,
  author = {Yiu, Thomas},
  title = {{SentinelShieldAI: LLM guard/security}},
  howpublished = {\url{[https://github.com/kyegomez/swarms](https://github.com/tomtyiu/SentinelShieldAI)}},
  year = {2024},
  note = {Accessed: Date}
}
