import xml.etree.ElementTree as ETree
import pandas as pd

# give the path where you saved the xml file
# inside the quotes
xmldata = "C: \\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\" \
          "Anaconda3(64 - bit)\\xmltopandas.xml"
prstree = ETree.parse(xmldata)
root = prstree.getroot()

# print(root)
store_items = []
all_items = []

for storeno in root.iter('store'):
    store_Nr = storeno.attrib.get('slNo')
    itemsF = storeno.find('foodItem').text
    price = storeno.find('price').text
    quan = storeno.find('quantity').text
    dis = storeno.find('discount').text

    store_items = [store_Nr, itemsF, price, quan, dis]
    all_items.append(store_items)

xmlToDf = pd.DataFrame(all_items, columns=[
    'SL No', 'ITEM_NUMBER', 'PRICE', 'QUANTITY', 'DISCOUNT'])

print(xmlToDf.to_string(index=False))
