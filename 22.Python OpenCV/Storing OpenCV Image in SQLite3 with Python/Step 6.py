# open the image you want to store in read more
im = open('gfg.png', 'rb').read()
conn.execute("INSERT INTO imgfg VALUES(?,?)",
			("pattern", sqlite3.Binary(im)))
