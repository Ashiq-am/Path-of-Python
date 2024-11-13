import camelot

# extract all the tables in the PDF file
abc = camelot.read_pdf("test.pdf") #address of file loation

# print the first table as Pandas DataFrame
print(abc[0].df)
