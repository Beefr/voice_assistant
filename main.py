from voiceAssistant import *


#from chatgptProcessing import ChatgptProcessing


def main():
    va= VoiceAssistant()
    while True:
        va.run()
    #c=ChatgptProcessing()
    #print(c.answer("salut Sarah"))
    #print(c.answer("quelle heure est-il stp?"))

if __name__ == "__main__":
    main()

