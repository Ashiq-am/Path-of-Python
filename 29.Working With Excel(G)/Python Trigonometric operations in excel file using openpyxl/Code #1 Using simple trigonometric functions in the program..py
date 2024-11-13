# import openpyxl module
import openpyxl

# Call a Workbook() function of openpyxl
# to create a new blank Workbook object
wb = openpyxl.Workbook()

# Get workbook active sheet
# from the active attribute.
sheet = wb.active

# set the width of the column
sheet.column_dimensions['A'].width = 20
sheet.column_dimensions['B'].width = 30
sheet.column_dimensions['C'].width = 20

# writing to the cell of an excel sheet
sheet['A1'] = "angles in radian"
sheet['A2'] = 0.1
sheet['A3'] = 0.2
sheet['A4'] = 0.3
sheet['A5'] = 0.4
sheet['A6'] = 0.5
sheet['A7'] = 0.6

# mention performing trigonometric operations
sheet['B1'] = "Applying trigonometric function"
sheet['B2'] = "Sine"
sheet['B3'] = "Cosine"
sheet['B4'] = "Tangent"
sheet['B5'] = "Cosecant"
sheet['B6'] = "Secant"
sheet['B7'] = "Cotangent"

# The value in cell C1 to C7 is set to a formula
# that calculates values for particular radian.
sheet['C1'] = 'corresponding values'
sheet['C2'] = '= SIN(0.1)'
sheet['C3'] = '= COS(0.2)'
sheet['C4'] = '= TAN(0.3)'
sheet['C5'] = '= CSC(0.4)'
sheet['C6'] = '= SEC(0.5)'
sheet['C7'] = '= COT(0.6)'

# save the file
wb.save("simple_trigonometric.xlsx")
