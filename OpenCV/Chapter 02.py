# How to convert image color
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                       #(image, RGB color ->  Grey color)

# How to convert to blur
imgBlur = cv2.GaussianBlur(img, (7,7), 0)                             # (image, kernel size, sigma_s)         
                                                                      # "Kernel" in computer vision are matrices(3x3, 7x7), used to perform some kind of convolution in our data.Kernels represent the area for each operation, the values/weights, and the anchor point.
                                                                      # "sigma_s" is controls how much the image is smoothed - the larger its value, the more smoothed the image gets, but it's also slower to compute.
# How to convert to canny
imgCanny = cv2.Canny(img, 100, 100)                                   # (image, threshold1, threshold2)       
                                                                      # first and second threshold for the hysteresis procedure. 


import numpy as np
kernel = np.ones((5,5), np.uint8)                                     # numpy.ones() function returns a new array of given shape and data type.

# How to change image dialation(thickness)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)             # iterations is Number of times dilation or erosion is applied
# How to change Image eroded(like before one)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


# How to change image value using trackbar

import cv2
import numpy as np

def empty(a):                                                    # This function is used to change trackbar everytime from user, what need to change
    pass
  
  
 # Create TrackBar

cv2.namedWindow("TrackBars")                                     # Create new window
cv2.resizeWindow("TrackBars", 640, 240)                          # Use "same name", using for resize
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)        # Create first trackbar  # (what value going to change[Hue = color], which window, min value, max value)
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 134, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)


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
 
    cv2.imshow("Mask image", maskImage)
    cv2.waitKey(1)

    
# Add color to image [using 2 images]
    
imgResult = cv2.bitwise_and(img, img, mask=maskImage)         # 2 images into 1 mage

cv2.imshow("Result image", imgResult)
cv2.waitKey(1)

