device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Initialize Generator, Discriminator, and Optimizers
generator = Generator()
discriminator = Discriminator()

optimizer_G = optim.Adam(generator.parameters(), lr=0.0002)
optimizer_D = optim.Adam(discriminator.parameters(), lr=0.0002)

# Load pre-trained VGG model for Perceptual Loss
vgg = models.vgg19(pretrained=True).to(device)
criterion_content = ContentLoss()
criterion_perceptual = PerceptualLoss(vgg)

# Train ESRGAN
train(generator, discriminator, dataloader, num_epochs=2, optimizer_G=optimizer_G, optimizer_D=optimizer_D,
      criterion_content=criterion_content, criterion_perceptual=criterion_perceptual, device=device)
