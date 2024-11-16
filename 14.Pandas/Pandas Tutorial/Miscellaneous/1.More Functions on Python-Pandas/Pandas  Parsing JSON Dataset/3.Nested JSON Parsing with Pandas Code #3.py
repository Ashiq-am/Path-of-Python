soloist_data = json_normalize(data = d['programs'],
							record_path =['works', 'soloists'],
							meta =['id'])

soloist_data.head(3)
