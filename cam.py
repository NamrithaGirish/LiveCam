#PYTHON CAMERA MODEL
import cv2
import numpy as np
i=0

#DEFINING CAPTURE ACTION
def capturing(event,x,y,flags,param):
    global i
    if event==cv2.EVENT_LBUTTONUP:
        name="photo_"+str(i)+".png"
        wname="CAPTURED IMAGE"
        cv2.imwrite(name,frame)
        h=cv2.imread(name)
        cv2.namedWindow(wname)
        cv2.imshow(wname,h)
        cv2.moveWindow(wname,700,50)
        i+=1
        cv2.waitKey(1000)
        cv2.destroyWindow(wname)

#WEBCAM ACCESSING
cap=cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    win="CAPTURE"
    cv2.imshow("CAMERA",frame)
    cv2.moveWindow("CAMERA",50,50)
    cv2.namedWindow(win)
    img=np.zeros((150,150,3))
    cv2.putText(img,"CLICK",(35,65),cv2.FONT_HERSHEY_SIMPLEX,0.85,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,"HERE",(35,90),cv2.FONT_HERSHEY_SIMPLEX,0.85,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow(win,img)
    cv2.moveWindow(win,250,600)
    cv2.setMouseCallback(win,capturing)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
