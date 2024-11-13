# Iterating through the pages
for current_page in range(len(docu)):

    # Getting the images in that page


    for image in docu.getPageImageList(current_page):
        # get the XREF of the image . XREF can be thought of a
        # container holding the location of the image
        xref = image[0]

        # extract the object i.e,
        # the image in our pdf file at that XREF

        pix = fitz.Pixmap(docu, xref)

        # Storing the image as .png
        pix.writePNG('page %s - %s.png' % (current_page, xref))
