import cv2
import numpy as np

img = cv2.imread("Resources/cat.jpg")

width, height = 250, 350
pts1 = np.float32([[494,139], [795, 133], [502, 467], [816, 452]])            # [top left][top right][bottom left][botton right]
pts2 = np.float32([[0,0], [width,0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)                              # getPerspectiveTransform() - It takes as input the 4 pairs of corresponding points on the image from which want to gather information by changing the perspective and pass it into .wrapPerspective() function.

OutputImage = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Display", img)
cv2.imshow("Output Image", OutputImage)
cv2.waitKey(0)
