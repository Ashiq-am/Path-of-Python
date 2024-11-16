import xml.etree.ElementTree as ETree
import pandas as pd

xmldata = '''<?xml version="1.0" encoding="UTF-8"?>
		<Food>
			<Info>
			<Msg>Food Store items.</Msg>
			</Info>
			<store slNo="1">
				<foodItem>meat</foodItem>
				<price>200</price>
				<quantity>1kg</quantity>
				<discount>7%</discount>
			</store>
			<store slNo="2">
				<foodItem>fish</foodItem>
				<price>150</price>
				<quantity>1kg</quantity>
				<discount>5%</discount>
			</store>
			<store slNo="3">
				<foodItem>egg</foodItem>
				<price>100</price>
				<quantity>50 pieces</quantity>
				<discount>5%</discount>
			</store>
			<store slNo="4">
				<foodItem>milk</foodItem>
				<price>50</price>
				<quantity>1 litre</quantity>
				<discount>3%</discount>
			</store>
		</Food>
'''

prstree = ETree.fromstring(xmldata)
root = prstree.tag

# print(root)
store_items = []
all_items = []

for storeno in prstree.findall('store'):
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
