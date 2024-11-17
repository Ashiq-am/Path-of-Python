#Function to generate hybrid image
#D0 is cutoff frequency
def hybrid_images(image1, image2, D0 = 50):
    original1 = np.fft.fft2(image1)                          #Get the fourier of image1
    center1 = np.fft.fftshift(original1)                     #Apply Centre shifting
    LowPassCenter = center1 * gaussianLP(D0, image1.shape)   #Extract low frequency component
    LowPass = np.fft.ifftshift(LowPassCenter)
    inv_LowPass = np.fft.ifft2(LowPass)                         #Get image using Inverse FFT

    original2 = np.fft.fft2(image2)
    center2 = np.fft.fftshift(original2)
    HighPassCenter = center2 * gaussianHP(D0, image2.shape)  #Extract high frequency component
    HighPass = np.fft.ifftshift(HighPassCenter)
    inv_HighPass = np.fft.ifft2(HighPass)
    hybrid = np.abs(inv_LowPass) + np.abs(inv_HighPass)      #Generate the hybrid image
    return hybrid
