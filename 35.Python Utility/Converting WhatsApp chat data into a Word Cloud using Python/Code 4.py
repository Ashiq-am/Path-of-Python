df = df.drop(columns = ['Convo'])
df[['Message']] = df['Message'].str.lower()
df['Message'] = df['Message'].str.replace('<media omitted>', 'Media Shared')
df['Message'] = df['Message'].str.replace('this message was deleted',
										'DeletedMsg')
