from torch.utils.tensorboard import SummaryWriter

dummy_input = torch.randn(1, 1, 28, 28)
writer = SummaryWriter('runs/simple_nn')
writer.add_graph(model, dummy_input)
writer.close()
