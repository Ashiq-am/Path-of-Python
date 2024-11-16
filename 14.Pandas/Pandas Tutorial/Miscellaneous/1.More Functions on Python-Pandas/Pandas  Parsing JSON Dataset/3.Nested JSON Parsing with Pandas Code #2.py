works_data = json_normalize(data = d['programs'],
							record_path ='works',
							meta =['id', 'orchestra', 'programID', 'season'])
works_data.head(3)
