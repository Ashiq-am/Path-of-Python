# Mask the lower triangle
masked_data_lower = np.ma.array(data, mask=lower_mask)

# Mask the upper triangle
masked_data_upper = np.ma.array(data, mask=upper_mask)
