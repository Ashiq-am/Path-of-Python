import cv2
import numpy as np


def process_on_gpu(image_part, gpu_id):
    # Set the GPU device
    cv2.cuda.setDevice(gpu_id)

    # Upload the image part to the GPU
    gpu_image = cv2.cuda_GpuMat()
    gpu_image.upload(image_part)

    # Perform Gaussian blur on the GPU
    gaussian_filter = cv2.cuda.createGaussianFilter(
        cv2.CV_8UC1, cv2.CV_8UC1, (15, 15), 0)
    gpu_blurred_image = gaussian_filter.apply(gpu_image)

    # Download the result back to the host
    result_image = gpu_blurred_image.download()

    return result_image


# Load an image in grayscale
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Split the image into two parts for two GPUs
height, width = image.shape
half_height = height // 2

image_part1 = image[:half_height, :]
image_part2 = image[half_height:, :]

# Process each part on different GPUs
result_part1 = process_on_gpu(image_part1, 0)  # GPU 0
result_part2 = process_on_gpu(image_part2, 1)  # GPU 1

# Combine the results
combined_result = np.vstack((result_part1, result_part2))

# Display the result
cv2.imshow('Blurred Image', combined_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
