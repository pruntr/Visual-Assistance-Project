import pytesseract
from PIL import Image
import cv2
import os
import random,string
from gtts import gTTS
from playsound import playsound
# print(1)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# print(1)

def image_speech():
    cam = cv2.VideoCapture(0)
    print(1)
    cv2.namedWindow("test")
    # video = cv2.VideoCapture("https://10.4.183.8:8080/video")
    # print(1)
    i = 0
    # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    # print(1)
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        # time.sleep(0.1)
        if not ret:
            break
        k = cv2.waitKey(33)
        if k==27:  #Press ESC to exit
            break
        elif k == 32: #Press space bar to enter
            cv2.imwrite('opencv'+str(i)+'.png', frame)
            image = Image.open('opencv'+str(i)+'.png')
            text = pytesseract.image_to_string(image)
       # print(type(text))
      #  print(text)
            if text:
                tts='tts'
                tts=gTTS(text)
                name=randomword(10)
                file=str(str(i) + '.mp3')
                tts.save(file)
                playsound(file)
                os.remove(file)
          #  print(text)
                os.remove('opencv'+str(i)+'.png')
                i += 1
            else:
                print("Please click the photo again")
    cam.release()
    cv2.destroyAllWindows()

def randomword(length):
    letters=string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

if __name__ == '__main__':
    image_speech()

