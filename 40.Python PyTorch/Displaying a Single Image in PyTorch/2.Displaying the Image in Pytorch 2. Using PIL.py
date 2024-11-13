from torchvision.transforms import ToPILImage

# Convert the tensor to a PIL image
to_pil = ToPILImage()
image_pil = to_pil(image_tensor)

# Display the image
image_pil.show()
image_pil.save("output_image.png")
