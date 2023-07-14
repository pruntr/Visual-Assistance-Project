import speech_recognition as sr
from playsound import playsound
import yolowebcam
import sys
from imagetospeech import image_speech
from yolowebcam import YOLO, detect_webcam





st1="Say 1 for live object detection,say 2 for images text to speech conversion,say 0 for exitfrom system"
st2="you said 1 for live object detection"
st3="you said 2 for images text to speech conversion"
      
st4="you said wrong option,please choose correct option"
st5="Could not understand audio,please say again"


r = sr.Recognizer()
def choices():
    while True:
        playsound('st1.mp3')

        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source,timeout=5)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                print('st5.mp3')
        if text=="1": 
                playsound('st2.mp3')
                detect_webcam(YOLO())
                
        elif text=="2" or text=="Tu":
                playsound('st3.mp3')
                image_speech()
                
                
        elif text=="0":
                print("Program stopped")
                sys.exit()
        else:
                playsound('st4.mp3')
                continue
# choices()
        
if __name__ == '__main__':
      choices()
