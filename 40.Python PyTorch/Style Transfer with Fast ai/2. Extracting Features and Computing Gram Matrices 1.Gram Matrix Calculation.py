from torch import Tensor
import torch.nn.functional as F

def gram(x: Tensor):
    "Compute Gram matrix from feature maps"
    n, c, h, w = x.shape
    x = x.view(n, c, -1)
    return (x @ x.transpose(1, 2)) / (c * w * h)

# Compute Gram matrices for the style features
im_grams = [gram(f) for f in im_feats]
