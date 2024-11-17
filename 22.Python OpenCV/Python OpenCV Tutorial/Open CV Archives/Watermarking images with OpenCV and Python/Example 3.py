# calculating coordinates of center
# calculating center, where we are going
# to place our watermark
center_y = int(h_img/2)
center_x = int(w_img/2)

# calculating from top, bottom, right and left
top_y = center_y - int(h_logo/2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo
left_x = center_x - int(w_logo/2)
