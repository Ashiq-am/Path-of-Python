import xlwings as xw

# Define a function to write "Hello, world" to cell A1
def hello_excel():
    wb = xw.Book.caller()
    wb.sheets[0].range('A1').value = 'Hello, world'
