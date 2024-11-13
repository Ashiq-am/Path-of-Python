def info(pdf_path):
    # used get method to get the pdf file
    response = requests.get(pdf_path)

    # responce.content generate binay code for
    # string function
    with io.BytesIO(response.content) as f:
        # initialized the pdf
        pdf = PdfFileReader(f)

        # all info about pdf
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f""" 
	Information about {pdf_path}: 

	Author: {information.author} 
	Creator: {information.creator} 
	Producer: {information.producer} 
	Subject: {information.subject} 
	Title: {information.title} 
	Number of pages: {number_of_pages} 
	"""
    print(txt)

    return information
