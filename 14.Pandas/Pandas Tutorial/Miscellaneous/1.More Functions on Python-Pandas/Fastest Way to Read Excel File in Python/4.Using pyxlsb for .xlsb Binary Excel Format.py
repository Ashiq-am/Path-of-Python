import pyxlsb

# Read .xlsb file
with pyxlsb.open_workbook('data.xlsb') as wb:
    with wb.get_sheet(1) as sheet:
        li = []
        for i in sheet.rows():
            li.append([item.v for j in row])
print(li[:5])