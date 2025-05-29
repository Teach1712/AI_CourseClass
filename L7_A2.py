import cv2

image= cv2.imread('example.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

resized_image = cv2.resize(gray_image, (200, 200))

cv2.imshow('Resized Grayscale Image', resized_image)

key=cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('resized_grayscale_image.jpg', resized_image)
    print("Image saved as 'resized_grayscale_image.jpg'")
else:
    print("Image not saved.")

cv2.destroyAllWindows()
print("Image dimensions:", resized_image.shape)






