import torch
import torch.optim as optim

# Two probability distributions
P = torch.tensor([0.2, 0.5, 0.3], requires_grad=True)
Q = torch.tensor([0.1, 0.7, 0.2])

# Optimizer
optimizer = optim.Adam([P], lr=0.01)

# Minimizing KL divergence
for _ in range(100):
    optimizer.zero_grad()
    kl_loss = F.kl_div(torch.log(Q), P, reduction='sum')
    kl_loss.backward()
    optimizer.step()

    print(f'KL Loss: {kl_loss.item()}')
