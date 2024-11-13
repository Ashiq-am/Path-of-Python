import openpyxl

# Load the workbook
wb = openpyxl.load_workbook("data_workbook.xlsx")

# Select the active sheet
sheet = wb.active

# Read and print the data
for row in sheet.iter_rows(min_row=1, max_row=3, values_only=True):
    print(row)
