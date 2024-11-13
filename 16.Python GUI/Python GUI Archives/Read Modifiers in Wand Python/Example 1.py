# Import Image from wand.image module
from wand.image import Image

# Read first page of pdf using Image() function
with Image(filename ='document.pdf[0]') as first_page:
    # convert pdf page to image file
    first_page.convert("png")

    # save final image
    first_page.save(filename = "first_page_image.png")
