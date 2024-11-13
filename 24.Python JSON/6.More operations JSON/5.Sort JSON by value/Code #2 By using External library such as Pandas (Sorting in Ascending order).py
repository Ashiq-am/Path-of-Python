from pandas.io.json import json_normalize

df = json_normalize(json_parse['Student'],
							'subject',
					['enrollment_no', 'name'])

df.sort_values(['code', 'grade', 'enrollment_no']).reset_index(drop=True)
