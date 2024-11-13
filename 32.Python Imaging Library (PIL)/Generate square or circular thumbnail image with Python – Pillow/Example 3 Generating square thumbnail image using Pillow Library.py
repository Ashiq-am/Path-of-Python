# importing necessary libraries
from PIL import Image, ImageDraw
import numpy as np


# function to generate squared image
def square_thumb(thum_img, width, height):
    # checking if height and width are
    # are equal then return image as it is
    if height == width:
        return thum_img

    # checking if height is greater than width
    elif height > width:

        # creating the new mask image of size i,e height of Image
        square_img = Image.new(thum_img.mode, (height, height))

        # pasting the original image on mask image
        # using paste() function to make it square
        square_img.paste(thum_img, ((height - width) // 2, 0))

        # returning the generated square image
        return square_img

    # if width is greater than height
    else:

        # creating the new mask image of size i,e width of Image
        square_img = Image.new(thum_img.mode, (width, width))

        # pasting the original image on mask image using paste()
        # function to make it square
        square_img.paste(thum_img, (0, (width - height) // 2))

        # returning the generated square image
        return square_img

    # main function


if __name__ == "__main__":
    # opening the image from the storage
    # using Image.open() function
    orig_img = Image.open('sebastian-molina.jpg')

    # extracting width and height of an
    # image from the image size
    w, h = orig_img.size

    # calling the function by passing
    # image width and height as a parameter
    sq_img = square_thumb(orig_img, w, h)

    # generating square thumbnail of
    # required size using thumbnail() function
    sq_img.thumbnail((400, 400))

    # saving the thumbnail using save function
    sq_img.save('Square_thumbnail.jpg')
