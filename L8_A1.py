import cv2
#To check version of cv2
#print(cv2.__version__)

image=cv2.imread('example.jpg')
cv2.namedWindow('Activity 1', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Activity 1', 800, 500)

#display the image
cv2.imshow('Activity 1', image)

#wait for a key press and close the window
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()

print("Image dimensions:", image.shape)

