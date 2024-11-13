import openpyxl

# Create a new Workbook
wb = openpyxl.Workbook()

# Select the active sheet
sheet = wb.active

# Write data to specific cells
sheet["A1"] = "Name"
sheet["B1"] = "Age"

sheet["A2"] = "Alice"
sheet["B2"] = 25

sheet["A3"] = "Bob"
sheet["B3"] = 30

# Save the workbook
wb.save("data_workbook.xlsx")
