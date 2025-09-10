

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, logging

import torch


path="openai-community/gpt2" 



tokenizer = AutoTokenizer.from_pretrained(path)

model = AutoModelForCausalLM.from_pretrained(path)
model.config.pad_token_id = tokenizer.eos_token_id
logging.set_verbosity_error()

#device = "cuda" if torch.cuda.is_available() else "cpu" 
#model.to(device)



#input_text = """
#Hello, you are Jarvis a voice assistant designed by Corentin RENAULT. Your job is to answer to the questions that you get asked.
#- Corentin RENAULT is a french engineer. He is expert in image processing, computer vision and devops. 
#- You answer concisely 
#- You structure your answer
#- You motivate your choices if needed
#- You never repeat the prompt given to you
#- You will be given a context to help you answer more precisely
#- The last line starting by "Master:" is the line that you should be answering to 
#If you understood your assignment and the rules, you can start by saying: "Hello master, how may I help you?".
#"""
input_text = ""


#history = input_text  + "\n"

print("Hello Master, how may I help you?")

while True:
    input_text = input()
    if input_text.lower() in ["quit", "exit", "q"]:
        break


    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)


    outputs = model.generate(
        **inputs, 
        max_new_tokens=10,     # longueur de réponse max
        do_sample=True,         # sampling plutot que greedy
        top_p=0.7,              # nucleus sampling
        temperature=0.7)        # controle de la creativite


    reponse = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    print(reponse)
    
    #user_input = input()
    #if user_input.lower() in ["quit", "exit", "q"]:
    #    break

    #history = history + "Jarvis:" + reponse + "\n" + "Master:" + user_input + "\n"
    #intput_text = history



#print(tokenizer.decode(outputs[0], skip_special_tokens=True))










