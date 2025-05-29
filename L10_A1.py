import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(image,title):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # Grayscale image
        plt.imshow(image, cmap='gray')
    else:  # Color image
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return

    # Convert to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a window for the trackbars
    display_image(grayscale_image, 'Original Grayscale Image')

    print("Select an Option : ")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Smoothing")
    print("6. Exit")

    while True:
        user_input=input("Enter your choice (1-6): ")
        if user_input == '1':
            # Sobel Edge Detection
            sobel_x = cv2.Sobel(grayscale_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(grayscale_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image(combined_sobel, 'Sobel Edge Detection')

        elif user_input == '2':
            # Canny Edge Detection
            print("Adjusting Canny thresholds... defaults are 100 and 200.")
            lower_thresh = int(input("Enter lower threshold : "))
            upper_thresh = int(input("Enter upper threshold : "))            
            edges=cv2.Canny(grayscale_image, lower_thresh, upper_thresh)
            display_image(edges, 'Canny Edge Detection')

        elif user_input == '3':
            # Laplacian Edge Detection
            laplacian_edges = cv2.Laplacian(grayscale_image, cv2.CV_64F)
            display_image(np.abs(laplacian_edges).astype(np.uint8), 'Laplacian Edge Detection')

        elif user_input == '4':
            # Gaussian Smoothing
            print("Applying Gaussian Smoothing with a kernel size of (5, 5).")
            while True:
                try:
                    kernel_size = int(input("Enter kernel size (odd number, e.g., 5): "))
                    if kernel_size % 2 == 1 and kernel_size > 1:
                        break
                    else:
                        print("Please enter a positive odd integer greater than 1.")
                except ValueError:
                    print("Invalid input. Please enter a single odd integer (e.g., 5).")
            blurred = cv2.GaussianBlur(grayscale_image, (kernel_size, kernel_size), 0)
            display_image(blurred, 'Gaussian Smoothing')

        elif user_input == '5':
            # Median Smoothing
            median_smoothed = cv2.medianBlur(grayscale_image, 5)
            display_image(median_smoothed, 'Median Smoothing')
        elif user_input == '6':
            print("Exiting the program.")
            break   
        else:
            print("Invalid choice. Please select a valid option (1-6).")
interactive_edge_detection('example.jpg')
