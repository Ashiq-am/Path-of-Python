# the name of the media file
filename = "gfg.png"

# upload the file
media = api.media_upload(filename)

# printing the dimensions
print("The width is : " + str(media.image['w']) + " pixels.")
print("The height is : " + str(media.image['h']) + " pixels.")
