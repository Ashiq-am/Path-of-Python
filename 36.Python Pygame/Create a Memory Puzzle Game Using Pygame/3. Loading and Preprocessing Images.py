# Load card back image from URL and convert to PNG format
response = requests.get(
    "https://media.geeksforgeeks.org/wp-content/uploads/20240311145552/geeksforgeeks.png")
image = Image.open(BytesIO(response.content))
image = image.convert("RGB")
with BytesIO() as img_bytes:
    image.save(img_bytes, "PNG")
    img_bytes.seek(0)
    card_back = pygame.image.load(img_bytes)

# Load card images from URLs and convert to PNG format
card_images = []
for url in image_urls:
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.convert("RGB")
    with BytesIO() as img_bytes:
        image.save(img_bytes, "PNG")
        img_bytes.seek(0)
        card_images.append(pygame.image.load(img_bytes))
