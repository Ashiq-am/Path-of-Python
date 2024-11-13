from openpyxl import Workbook

# Create a new workbook
wb = Workbook()

# Access the active sheet
sheet = wb.active

# Rename the sheet (optional)
sheet.title = "DataSheet"

# Adding headers to the sheet
sheet["A1"] = "Name"
sheet["B1"] = "Age"

# Inserting rows of data
data = [
    ["POONAM", 28],
    ["MONA", 24],
    ["SITA", 30]
]

for row in data:
    sheet.append(row)

# Save the workbook with a custom filename
wb.save("example_project.xlsx")

print("Workbook saved successfully!")
