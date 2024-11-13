model = OvercompleteAutoencoder(input_dim=784, hidden_dim=1000)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
