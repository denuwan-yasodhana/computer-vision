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
