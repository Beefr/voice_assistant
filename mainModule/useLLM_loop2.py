

from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, logging

import torch


class LLM(object):

    def __init__(self):


        self._path="openai-community/gpt2" 

        self._tokenizer = AutoTokenizer.from_pretrained(self._path)

        self._model = AutoModelForCausalLM.from_pretrained(self._path)
        self._model.config.pad_token_id = self._tokenizer.eos_token_id
        logging.set_verbosity_error()
    
        self._response = "Hello Master, how may I help you?"

    @property
    def response(self):
        return self._response

    def answer(self, input_text):
        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)


        outputs = model.generate(
            **inputs, 
            max_new_tokens=10,     # longueur de réponse max
            do_sample=True,         # sampling plutot que greedy
            top_p=0.7,              # nucleus sampling
            temperature=0.7)        # controle de la creativite


        self._response = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
    
