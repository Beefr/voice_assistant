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

