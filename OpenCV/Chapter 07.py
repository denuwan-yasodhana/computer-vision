import cv2
import numpy as np

path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()                     # Get copy of image


# To find the Contours
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)   
    
    for cnt in contours:
        area = cv2.contourArea(cnt)          # Find the area
        print(area)

        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)                           # To draw the contours          
           
            peri = cv2.arcLength(cnt,True)                                                  # This need for get correct clear corner
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)                                   # This need for get correct clear corner
            print(len(approx))
             
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
 
            if objCor ==3:                                                                   # To find triangles
                objectType ="Triagles"                                               
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03: 
                    objectType= "Square"                                                     # To find squares
                else:
                    objectType="Rectangle"                                                   # To find rectangles
            elif objCor>4: 
                objectType= "Circles"                                                        # To find circles
            else:
                objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)                           # Make rectangle border arrounding each objects
            
            cv2.putText(imgContour,objectType,                                              # Display text on contour
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

            
cv2.imshow("Full details image", imgContour)
cv2.waitKey(0)

