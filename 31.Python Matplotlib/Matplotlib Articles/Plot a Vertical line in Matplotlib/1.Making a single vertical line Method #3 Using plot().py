# importing library
import matplotlib.pyplot as plt

# defining plot size
plt.figure(figsize = (10, 5))

# specifying plot coordinates
plt.plot((0, 0), (0, 1), scaley = False)

# setting scaley = True will make the line fit
# withn the frame, i.e It will appear as a finite line
plt.show()
