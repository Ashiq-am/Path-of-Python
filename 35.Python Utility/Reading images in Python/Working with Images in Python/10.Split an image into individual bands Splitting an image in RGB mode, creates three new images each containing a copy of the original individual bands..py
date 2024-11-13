from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("picture.jpg")

        # splitting the image
        print(img.split())
    except IOError:
        pass


if __name__ == "__main__":
    main()
