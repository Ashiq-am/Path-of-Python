import openpyxl

# Load the existing workbook
wb = openpyxl.load_workbook("data_workbook.xlsx")

# Select the active sheet
sheet = wb.active

# Modify the value in a specific cell
sheet["B2"] = 26

# Save the changes
wb.save("data_workbook_modified.xlsx")
