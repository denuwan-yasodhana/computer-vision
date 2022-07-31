import cv2
 
// Read the Image /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


img = cv2.imread("path_of_the_image_with_extension/")	            // Get image

cv2.imshow("name_of_the_window",img)	                            // Show image
cv2.waitKey(0) 				                                            // Delay time(milliseconds)



// Read the Video /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture("path_of_the_video with .mp4/")
 
while True:
    success, img = cap.read()

    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("name_of_the_window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):	                  // When press 'q', break the loop
        break
        

        
// Read the Webcam ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
  
 frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)                                   // To get default webcam
// cap = cv2.VideoCapture(ID) 	                            // use another webcam, type its "ID"

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)	                                          // 150 = Brightness of the camera

while True:
    success, img = cap.read()

    cv2.imshow("name_of_the_window", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):                   // When press 'q', break the loop
        break 
  
  
