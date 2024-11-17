""""""


'''
// writing the image to a defined location as JPEG 
bool check = imwrite("..path\\MyImage.jpg", img); 

// if the image is not saved 
if (check == false) { 
	cout << "Mission - Saving the image, FAILED" << endl; 

	// wait for any key to be pressed 
	cin.get(); 
	return -1; 
} 

cout << "Successfully saved the image. " << endl; 

'''