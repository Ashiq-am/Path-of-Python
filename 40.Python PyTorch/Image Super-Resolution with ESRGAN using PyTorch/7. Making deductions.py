def upscale_image(generator, lr_image):
    generator.eval()
    with torch.no_grad():
        sr_image = generator(lr_image)
    return sr_image
