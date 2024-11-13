from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("picture.jpg")

        # transposing image
        transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # Save transposed image
        transposed_img.save("transposed.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()
