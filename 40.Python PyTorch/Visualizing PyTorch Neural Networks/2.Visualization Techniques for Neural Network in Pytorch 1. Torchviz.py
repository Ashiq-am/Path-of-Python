from torchviz import make_dot

x = torch.randn(1, 28 * 28)
y = model(x)
make_dot(y, params=dict(model.named_parameters())).render("simple_nn", format="png")
