# Example input tensor
x = torch.rand(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)

# Self-attention
attn_output, attn_output_weights = multihead_attn(x, x, x)
attn_output, attn_output_weights
