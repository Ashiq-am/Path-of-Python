# Selection sort loop
while sorted_idx < arr_len - 1:
	min_idx = unsorted_idx
	for i in range(unsorted_idx, arr_len):
		if arr[i] < arr[min_idx]:
			min_idx = i
	arr[unsorted_idx], arr[min_idx] = arr[min_idx], arr[unsorted_idx]
	sorted_idx = unsorted_idx
	unsorted_idx += 1

	# Draw bars
	win.fill((0, 0, 0))
	for i in range(arr_len):
		color = (255, 255, 255) if i <= sorted_idx else (255, 0, 0)
		pygame.draw.rect(win, color,
				(i * (win_width / arr_len), win_height - arr[i],
						win_width / arr_len, arr[i]))
	pygame.display.update()
