from pil.Image import Image


def main():
    try:
        # Relative Path
        img = Image.open("picture.jpg")

        # In-place modification
        img.thumbnail((200, 200))

        img.save("thumb.jpg")
    except IOError:
        pass


if __name__ == "__main__":
    main()
