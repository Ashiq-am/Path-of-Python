attn_mask = torch.triu(torch.ones(10, 10), diagonal=1)  # Upper triangular matrix

attn_output, attn_output_weights = multihead_attn(query, key, value, attn_mask=attn_mask)
attn_output, attn_output_weights
