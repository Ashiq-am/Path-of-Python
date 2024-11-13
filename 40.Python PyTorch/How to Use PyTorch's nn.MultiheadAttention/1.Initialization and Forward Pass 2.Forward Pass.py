query = torch.rand(10, 32, embed_dim)  # (sequence_length, batch_size, embed_dim)
key = torch.rand(10, 32, embed_dim)
value = torch.rand(10, 32, embed_dim)

attn_output, attn_output_weights = multihead_attn(query, key, value)
