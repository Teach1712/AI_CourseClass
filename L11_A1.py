import cv2
import numpy as np

def apply_color_filter(image,filter_type):
    filtered_image=image.copy()
    if filter_type == 'original':
        return filtered_image
    elif filter_type == 'red_tint':
        filtered_image[:, :,1] = 0
        filtered_image[:, :, 0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'green_tint':
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0
    elif filter_type == 'increase_red':
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)
    elif filter_type == 'decrease_blue':
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    else:
        return filtered_image
    
image_path=r"C:\Users\Dell\Desktop\Python\AI_CourseClass\Visionary AI - I\Lesson11\example.jpg"
image= cv2.imread(image_path)

if image is None:
    print("Error: Could not read the image.")
else:
    filter_type = 'original'
    print("Press the following keys to apply filters:")
    print("R- Red Tint")
    print("B- Blue Tint")
    print("G- Green Tint")
    print("I- Increase Red Intensity")
    print("D- Decrease Blue Intensity")
    print("Q- Quit")


    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow('Filtered Image', filtered_image)  # Show the image window
        print(f"Filtered image type: {type(filtered_image)}, shape: {getattr(filtered_image, 'shape', None)}")
        key = cv2.waitKey(0) & 0xFF

        if key == ord('o'):
            filter_type = 'original'
        elif key == ord('r'):
            filter_type = 'red_tint'
        elif key == ord('b'):
            filter_type = 'blue_tint'
        elif key == ord('g'):
            filter_type = 'green_tint'
        elif key == ord('i'):
            filter_type = 'increase_red'
        elif key == ord('d'):
            filter_type = 'decrease_blue'
        elif key == ord('q'):
            print("Exiting...")
            break

cv2.destroyAllWindows()


