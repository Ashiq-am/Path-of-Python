import openpyxl

# Create a new Workbook
wb = openpyxl.Workbook()

# Select the active sheet
sheet = wb.active

# Write data
sheet["A1"] = 10
sheet["A2"] = 20

# Add a formula
sheet["A3"] = "=A1 + A2"

# Save the workbook
wb.save("formula_workbook.xlsx")
