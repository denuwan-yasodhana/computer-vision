import cv2

img = cv2.imread("Resources/image.jpg")

# to get image size
print(img.shape)    #  (height, width, no of your channels for each pixel (Red, Green, Blue))

# How to resize the image
imgResize = cv2.resize(img, (250,150))         # (image, (width, height))

# How to crop the image
imgCrop = img[0:100, 200:500]    # [height(start raw : end row), width(start column : end column)]


cv2.imshow("Display", img)
cv2.imshow("Resized image", imgResize)
cv2.waitKey(0)
