import cv2 as cv
import os

n = 1000

camera = cv.VideoCapture(0)
sets = ['train', 'val']
label = ["ThumbsUp", "ThumbsDown"]


for i in sets:
    if not os.path.exists("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/"+i):
        os.mkdir("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/"+i)


for l in label:
    if not os.path.exists("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/train/"+l):
        os.mkdir("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/train/"+l)

    if not os.path.exists("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/val/"+l):
        os.mkdir("/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/val/"+l)

for folder in label:
    count = 0
    print("Press 'x' to collect data for",folder)
    userinput = input()
    if userinput != 'x':
        exit()
    while count<n:
        status, frame = camera.read()
        g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow(folder,g)
        g = cv.resize(g, (200,200))
        cv.imwrite('/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/train/'+folder+'/'+ str(count)+'.png',g)
        count+=1
        if cv.waitKey(1) == ord('q'):
            break
    count = 0
    while count<(n*0.2):
        status, frame = camera.read()
        g = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow(folder,g)
        g = cv.resize(g, (200,200))
        cv.imwrite('/Users/rohanrichard/Desktop/Code/Computer-Vision/Face-Recogniser/Face-Recogniser/val/'+folder+'/'+str(count)+'.png',g)
        count+=1
        if cv.waitKey(1) == ord('q'):
            break

camera.release()
cv.destroyAllWindows()