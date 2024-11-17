import cv2
import numpy as np
import time


def main():
    # Check if CUDA is available
    if not cv2.cuda.getCudaEnabledDeviceCount():
        print("CUDA is not available. Please ensure you have a CUDA-capable GPU and the correct drivers installed.")
        return

    # Initialize CUDA device
    device_count = cv2.cuda.getCudaEnabledDeviceCount()
    print(f"Number of CUDA-capable GPUs: {device_count}")

    # Read the image
    image_path = 'path_to_your_image.jpg'
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found.")
        return

    # Function to perform GPU processing on an image
    def process_image_on_gpu(image, device_id):
        cv2.cuda.setDevice(device_id)

        # Upload the image to the GPU
        gpu_image = cv2.cuda_GpuMat()
        gpu_image.upload(image)

        # Apply Gaussian blur on the GPU
        gpu_blur = cv2.cuda.createGaussianFilter(
            gpu_image.type(), -1, (15, 15), 0)
        gpu_blurred_image = gpu_blur.apply(gpu_image)

        # Download the result back to the CPU
        result_image = gpu_blurred_image.download()
        return result_image

    # Measure performance
    start_time = time.time()

    # Process image on GPU 0
    result_image_gpu0 = process_image_on_gpu(image, 0)

    # If multiple GPUs are available, process on GPU 1 as well
    if device_count > 1:
        result_image_gpu1 = process_image_on_gpu(image, 1)

    total_gpu_time = time.time() - start_time

    # Display processing time
    print(f"Total GPU Processing Time: {total_gpu_time:.6f} seconds")

    # Display the original and blurred images
    cv2.imshow('Original Image', image)
    cv2.imshow('Blurred Image (GPU 0)', result_image_gpu0)
    if device_count > 1:
        cv2.imshow('Blurred Image (GPU 1)', result_image_gpu1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
