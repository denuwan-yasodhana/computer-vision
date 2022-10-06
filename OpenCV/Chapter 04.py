import cv2
import numpy as np

# Create black image
img = np.zeros((512,512))                       # .zero(shape, data type) - It is used to create an array based on the particular shape or type. This function is similar to .ones() function
print(img.shape)                                # (512, 512)   No- no of channels
cv2.imshow("Display", img)
cv2.waitKey(0)


# Create RGB color image
img = np.zeros((512,512, 3), np.uint8)

img[:] = 255, 0, 0                              # Whole image is blue
img[200:300, 100:300] = 255, 0, 0               # Part of image is blue


# Make a line
cv2.line(img, (0,0), (300, 300), (0, 255, 0), 3)                          # (image, starting point, ending point, color, thickness)
cv2.line(img, (0,5), (img.shape[1], img.shape[0]), (255, 0, 0), 3)        # (image, starting point, (width, height), color, thickness)


# Make rectangle
cv2.rectangle(img, (0,0), (300, 300), (255, 0, 0), 3)                     # (image, starting point, ending point, color, thickness)
cv2.rectangle(img, (0,0), (300, 300), (0, 0, 255), cv2.FILLED)


#Make circule
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)                          # (image, center point, radius, color, thickness)

# How to put text
cv2.putText(img, "Denuwan Yasodhana", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 1)     # (image, text, location, font face, font size, color, thickness)




