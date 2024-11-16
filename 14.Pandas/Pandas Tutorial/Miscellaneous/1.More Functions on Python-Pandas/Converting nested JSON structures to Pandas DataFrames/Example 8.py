pd.json_normalize(data, record_path=['employees'], meta=[
				'company', 'location', ['info', 'president']])
