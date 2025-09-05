

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

import torch


path="openai-community/gpt2" #do not use please
#path = "../gpt2/"



tokenizer = AutoTokenizer.from_pretrained(path)

model = AutoModelForCausalLM.from_pretrained(path)



#device = "cuda" if torch.cuda.is_available() else "cpu" 
#model.to(device)



input_text = "Bonjour, tu as été inventé par Corentin RENAULT, qui t'a inventé?"

 

inputs = tokenizer(input_text, return_tensors="pt").to(model.device)


outputs = model.generate(**inputs, max_new_tokens=500)

print(tokenizer.batch_decode(outputs, skip_special_tokens=True)[0])

#print(tokenizer.decode(outputs[0], skip_special_tokens=True))










