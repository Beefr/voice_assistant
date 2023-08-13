from mainModule.voiceAssistant import *

import sounddevice

def main():
    camera=True
    soundInput=True
    soundOutput=True 
    chatGPT = False
    va= VoiceAssistant(camera, soundInput, soundOutput, chatGPT)
    va.run()

if __name__ == "__main__":
    main()



# ce serait bien de rajouter:
    # detection des obstacles                   <=== nécessite avertissement sonore
    # detection des radars                      <=== nécessite avertissement sonore
    # detection des visages                     <=== ez mais 
    # reconnaissance faciale                    <=== aie
    # envoi de mails                            <=== plutôt de notifications 
    # faudrait faire une presentation de ce qui est capturé
