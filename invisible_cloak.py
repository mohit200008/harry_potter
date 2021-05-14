import cv2
import numpy as np

cap= cv2.VideoCapture(0)
back= cv2.imread('./image.jpg')

while cap.isOpened():
    #take each frame
    ret,frame= cap.read()

    if ret: 
        # convert rgb into hsv?
        hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #cv2.imshow("hsv",hsv)
        #how to get hsv value?
        #lower: hue -10,100,100,higher:h+10,255,255
        red= np.uint8([[[0,0,255]]])
        hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
        #print(hsv_red)

        l_red= np.array([0,100,100])
        h_red=np.array([10,255,255])

        mask= cv2.inRange(hsv,l_red,h_red)
       

        part1= cv2.bitwise_and(back,back,mask=mask)
        #cv2.imshow("part1",part1)

        part2= cv2.bitwise_and(frame,frame,mask=mask)
        
        cv2.imshow("cloak", part1+part2)


        if cv2.waitKey(5)== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()        