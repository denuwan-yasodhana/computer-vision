import cv2
import numpy as np

def empty(a):               # This function is used to change trackbar everytime from user, what need to change
    pass
  
  
 # Change color using TrackBar

cv2.namedWindow("TrackBars")                                     # Create new window
cv2.resizeWindow("TrackBars", 640, 240)                          # Use "same name", using for resize
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)        # Create first trackbar  # (what value going to change[Hue = color], which window, min value, max value)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 134, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)


# How to change image value using trackbar

while True:
    img = cv2.imread("Resources/image.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")            # Get values to variable
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    maskImage = cv2.inRange(imgHSV, lower, upper)                 # Set values to image
    
    
    # Add color to image [using 2 images]
    
    imgResult = cv2.bitwise_and(img, img, mask=maskImage)         # 2 images into 1 mage
    
    
    
    cv2.imshow("Original", img)
    cv2.imshow("HSV color image", imgHSV)
    cv2.imshow("Mask image", maskImage)
    cv2.imshow("Result image", imgResult)
    cv2.waitKey(1)
    
