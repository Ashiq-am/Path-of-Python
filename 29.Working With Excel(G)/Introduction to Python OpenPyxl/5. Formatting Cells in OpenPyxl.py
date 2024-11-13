from openpyxl import Workbook
from openpyxl.styles import Font

# Create a new Workbook
wb = Workbook()

# Select the active sheet
sheet = wb.active

# Write data with formatting
sheet["A1"] = "Formatted Text"

 # Red, bold, size 14 font
sheet["A1"].font = Font(size=14, bold=True, color="FF0000")

# Save the workbook
wb.save("formatted_workbook.xlsx")
