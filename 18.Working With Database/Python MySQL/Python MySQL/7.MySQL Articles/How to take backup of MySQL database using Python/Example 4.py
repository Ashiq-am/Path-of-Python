for table_name in table_names:
	cursor.execute(
		f'CREATE TABLE {table_name} SELECT * FROM {db}.{table_name}')
