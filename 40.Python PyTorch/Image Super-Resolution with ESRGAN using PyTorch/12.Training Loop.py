def train(generator, discriminator, dataloader, num_epochs, optimizer_G, optimizer_D, criterion_content,
          criterion_perceptual, device):
    generator.to(device)
    discriminator.to(device)

    for epoch in range(num_epochs):
        for i, img in enumerate(dataloader):
            img = img.to(device)

            # Generate super-resolved image
            sr_image = generator(img)

            # Train Generator
            optimizer_G.zero_grad()
            content_loss = criterion_content(sr_image, img)
            perceptual_loss = criterion_perceptual(sr_image, img)
            g_loss = content_loss + perceptual_loss
            g_loss.backward()
            optimizer_G.step()

            # Train Discriminator
            optimizer_D.zero_grad()
            real_output = discriminator(img)
            fake_output = discriminator(sr_image.detach())
            d_loss = F.binary_cross_entropy_with_logits(real_output, torch.ones_like(real_output)) + \
                     F.binary_cross_entropy_with_logits(fake_output, torch.zeros_like(fake_output))
            d_loss.backward()
            optimizer_D.step()

            if i % 10 == 0:
                print(f"Epoch {epoch}/{num_epochs}, Step {i}, G Loss: {g_loss.item()}, D Loss: {d_loss.item()}")
