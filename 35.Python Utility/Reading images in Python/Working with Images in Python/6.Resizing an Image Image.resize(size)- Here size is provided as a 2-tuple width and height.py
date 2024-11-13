from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("picture.jpg")
        width, height = img.size

        img = img.resize((width / 2, height / 2))

        # Saved in the same relative location
        img.save("resized_picture.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()
