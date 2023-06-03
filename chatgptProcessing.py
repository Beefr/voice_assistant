import openai
from pathlib import Path


class ChatgptProcessing(object):

    def __init__(self):
        self.readApiKey()

        self._messages=[]
        self._system="Voici ta liste de contrôle. 1. contexte: tu es mon home assistant Sarah, et je suis Corentin, tu peux m'appeler monsieur. 2. objectif: Tu dois répondre à mes questions de manière courte et précise tout en étant extrêmement respectueux, comme un majordome. 3. règles: si tu ne comprends pas, dis pourquoi tu ne comprends pas. Evite les messages trop longs. Dis ok si je te donne une consigne."
        self._messages.append({'role': 'system', 'content': self._system})
        
        self._response=openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self._messages
        )
        self._messages.append(self._response.choices[0].message)
        
    def readApiKey(self):
        p = Path(__file__).with_name('key.txt')
        with open(p, "r") as f:
            key = f.read()
            f.close()
        openai.api_key=key

    @property
    def response(self):
        return self._response

    def answer(self, text):
        self._messages.append({'role': 'user', 'content': text})
        self._response=openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self._messages
        ).choices[0].message
        #print(self._response.content)
        self._messages.append(self._response)
        #print(self._messages)