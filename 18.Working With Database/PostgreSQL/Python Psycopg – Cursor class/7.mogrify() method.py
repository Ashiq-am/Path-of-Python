# cursor.mogrify() to insert multiple values
args = ','.join(cursor.mogrify("(%s,%s,%s)", i).decode('utf-8')
				for i in values)
