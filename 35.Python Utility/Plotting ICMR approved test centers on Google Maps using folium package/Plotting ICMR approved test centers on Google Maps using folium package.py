import folium

import pandas as pd

phone_map = folium.Map(location=[20.5937, 78.9629],
					zoom_start=4.4)
df = pd.DataFrame(pd.read_csv('ICMRTestingLabsWithCoords.csv'))

locate = {}

for i, j, k, l in zip(df['latitude'], df['longitude'],
					df['lab'], df['type']):

	temp = []
	temp.extend((i, j))
	locate['loc'] = temp
	marker = folium.Marker(location=locate['loc'],
						popup=str(k)+' Type:'+str(l))

	marker.add_to(phone_map)

phone_map
