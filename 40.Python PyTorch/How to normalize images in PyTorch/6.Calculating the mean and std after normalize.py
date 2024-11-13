# Python code to calculate mean and std
# of normalized image

# get normalized image
img_nor = transform_norm(img)

# cailculate mean and std
mean, std = img_nor.mean([1,2]), img_nor.std([1,2])

# print mean and std
print("Mean and Std of normalized image:")
print("Mean of the image:", mean)
print("Std of the image:", std)
