from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Activation
from keras.layers import BatchNormalization as BatchNorm
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
import cv2
from tensorflow import keras

classifier = cv2.CascadeClassifier('/Users/rohanrichard/miniforge3/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')
vid = cv2.VideoCapture(0)
  
while(True):
    ret, frame = vid.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(frame, scaleFactor=1.3, minNeighbors=5)
    
    width  = vid.get(3)
    height = vid.get(4)

    for (x, y, w, h) in faces:
        color = (255, 0, 255) # in BGR
        stroke = 5
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, stroke)
        s = "Number of people in frame: "+ str(len(faces))
        cv2.putText(frame,s, (0,50), 2, 2, (255,255,255))

    cv2.imshow('Smile!', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
vid.release()
cv2.destroyAllWindows()