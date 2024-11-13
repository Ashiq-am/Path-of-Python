# Lower triangle mask
lower_mask = np.tri(data.shape[0], data.shape[1], k=-1)

# Upper triangle mask
upper_mask = lower_mask.T
