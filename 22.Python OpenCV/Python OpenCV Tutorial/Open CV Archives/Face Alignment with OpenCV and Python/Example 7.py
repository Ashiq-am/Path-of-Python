# scale the image
test_set = ["pic.png"]
for i in test_set:
	alignedFace = Face_Alignement(i)
	pl.imshow(alignedFace[:, :, ::-1])
	pl.show()
	img, gray_img = face_detection(alignedFace)
	pl.imshow(img[:, :, ::-1])
	pl.show()
