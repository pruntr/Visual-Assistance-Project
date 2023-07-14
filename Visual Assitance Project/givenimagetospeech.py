import pytesseract
from PIL import Image
import cv2
import os
import random,string
from gtts import gTTS
from playsound import playsound

# specify the path to the image file
image_path = 'C:/Users/praga/Downloads/EPICS-main (1)/EPICS-main/YOLO/opencv0.png'



# load the image using Pillow
image = Image.open(image_path)

# apply OCR using pytesseract
def image_speech():
    text = pytesseract.image_to_string(image)
    i=0
    if text:
        tts='tts'
        tts=gTTS(text)
        name=randomword(10)
        file=str(str(i) + '.mp3')
        tts.save(file)
        playsound(file)
        os.remove(file)
        i+=1
    print(text)
    

def randomword(length):
    letters=string.ascii_lowercase
    print(letters)

    return ''.join(random.choice(letters) for i in range(length))

# print the extracted text
if __name__ == '__main__':
    image_speech()
