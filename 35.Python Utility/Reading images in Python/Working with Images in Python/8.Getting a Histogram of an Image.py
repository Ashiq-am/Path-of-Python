def main():
    try:
        # Relative Path
        img = Image.open("picture.jpg")

        # Getting histogram of image
        print(img.histogram())

    except IOError:
        pass


if __name__ == "__main__":
    main()
