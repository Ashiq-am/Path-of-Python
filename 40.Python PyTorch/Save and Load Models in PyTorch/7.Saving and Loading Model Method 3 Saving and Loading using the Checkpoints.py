# Saving the model
checkpoint = {
	'epoch': epoch,
	'model_state_dict': cnn_model.state_dict(),
	'optimizer_state_dict': optimizer.state_dict(),
	'loss': loss,
	# you may add other information to add
}
torch.save(checkpoint, 'checkpoint.pth')

# Loading the model
checkpoint = torch.load('checkpoint.pth')
cnn_model = SimpleCNN()
cnn_model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']
print(cnn_model)
