if uploaded_file is not None:
	file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
	img = cv2.imdecode(file_bytes, 1)
	st.image(seam_carve(img, new_width, new_height), channels="BGR")
