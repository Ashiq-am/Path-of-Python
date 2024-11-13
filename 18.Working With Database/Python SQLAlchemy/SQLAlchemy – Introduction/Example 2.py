db.select([films]).where(db.and_(films.columns.certification == 'R',
								films.columns.release_year > 2003))
