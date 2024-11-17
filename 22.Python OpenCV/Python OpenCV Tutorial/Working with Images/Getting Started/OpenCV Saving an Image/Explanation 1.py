""""""

'''
// Reading the image file from a given location in system 
Mat img = imread("..path\\abcd.jpg"); 

// if there is no image 
// or in case of error 
if (img.empty()) { 
	cout << "Can not open or image is not present" << endl; 

	// wait for any key to be pressed 
	cin.get(); 
	return -1; 
} 

'''