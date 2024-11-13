# import openpyxl module
import openpyxl

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute
sheet = wb.active

# One can change the name of the title
sheet.title = "sheet1"

print("sheet name is renamed as: " + sheet.title)
