from mainModule.voiceAssistant import *



def main():
    camera=True
    soundInput=True
    soundOutput=False
    va= VoiceAssistant(camera, soundInput, soundOutput)
    while True:
        va.run()

if __name__ == "__main__":
    main()



# ce serait bien de rajouter:
    # detection des obstacles                   <=== nécessite avertissement sonore
    # detection des radars                      <=== nécessite avertissement sonore
    # detection des visages                     <=== ez mais 
    # reconnaissance faciale                    <=== aie
    # envoi de mails                            <=== plutôt de notifications 
    # enregistrement video de -10sec à stop
    # faudrait faire une presentation de ce qui est capturé