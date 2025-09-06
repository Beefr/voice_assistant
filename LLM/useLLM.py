

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

import torch


path="openai-community/gpt2" 



tokenizer = AutoTokenizer.from_pretrained(path)

model = AutoModelForCausalLM.from_pretrained(path)
model.config.pad_token_id = model.config.eos_token_id


#device = "cuda" if torch.cuda.is_available() else "cpu" 
#model.to(device)



input_text = "Hello, you are a voice assistant designed by Corentin RENAULT, a french engineer expert in image processing, computer vision and devops."

 

inputs = tokenizer(input_text, return_tensors="pt").to(model.device)


outputs = model.generate(
        **inputs, 
        max_new_tokens=100,     # longueur de réponse max
        do_sample=True,         # sampling plutot que greedy
        top_p=0.9,              # nucleus sampling
        temperature=0.7)        # controle de la creativite

print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])

#print(tokenizer.decode(outputs[0], skip_special_tokens=True))










