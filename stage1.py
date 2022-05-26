import cv2
import math

video = cv2.VideoCapture("bb3.mp4")


tracker = cv2.TrackerCSRT_create()

returned,img = video.read()

bbox = cv2.selectROI("Tracking",img,False)

tracker.init(img,bbox)

print(bbox)

def drawBox(img,bbox):
    
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,0),3)
    
    cv2.putText(img,"Tracking",(80,90),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)
    

while True:
    check,img = video.read()
    
    success,bbox = tracker.update(img)
    
    
    if(success):
        drawBox (img,bbox)
    else:
        cv2.putText(img,"lost",(80,90),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)

    cv2.imshow("result",img)
    
    
    
    
    key = cv2.waitKey(20)
    
    if key==32 :
        print("stopped")
        break
    
video.release()
cv2.destroyAllWindows()