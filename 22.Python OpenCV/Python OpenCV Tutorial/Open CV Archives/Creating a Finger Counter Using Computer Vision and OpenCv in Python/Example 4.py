"""
# Enter key 'q' to break the loop
if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release
# the capture and destroy the windows
video.release()
cv2.destroyAllWindows()



"""