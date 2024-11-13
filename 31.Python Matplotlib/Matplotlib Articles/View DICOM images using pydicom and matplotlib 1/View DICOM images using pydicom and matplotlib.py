import matplotlib.pyplot as plt
import pydicom
import pydicom.data

# Full path of the DICOM file is passed in base
base = r"C:\Users\Ajit Gupta\Documents\dicom image"
pass_dicom = "1-12.dcm" # file name is 1-12.dcm

# enter DICOM image name for pattern
# result is a list of 1 element
filename = pydicom.data.data_manager.get_files(base, pass_dicom)[0]

ds = pydicom.dcmread(filename)

plt.imshow(ds.pixel_array, cmap=plt.cm.bone) # set the color map to bone
plt.show()
