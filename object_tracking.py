import cv2
import time
import math

video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()

# Read the first frame of the video
returned, img = video.read()

# Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)

print(bbox)

def drawBox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(25,150,200),3)
    cv2.putText(img,"Tracking ",(80,100),cv2.FONT_ITALIC,0.5,(250,189,25),2)

while True:
    check,img = video.read() 
    sucess,bbox=tracker.update(img)
    if sucess:
        drawBox(img,bbox)
    else:
            cv2.putText(img,"Not Found   ",(80,100),cv2.FONT_ITALIC,0.5,(250,189,25),2)


    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()







