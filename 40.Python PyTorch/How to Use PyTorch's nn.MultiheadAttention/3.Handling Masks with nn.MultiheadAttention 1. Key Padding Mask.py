key_padding_mask = torch.zeros(32, 10, dtype=torch.bool)  # (batch_size, sequence_length)
key_padding_mask[:, 5:] = 1  # Mask out positions after the 5th token

attn_output, attn_output_weights = multihead_attn(query, key, value, key_padding_mask=key_padding_mask)
attn_output, attn_output_weights
