import torch
import torch.nn as nn

embed_dim = 256
num_heads = 8
multihead_attn = nn.MultiheadAttention(embed_dim, num_heads)
