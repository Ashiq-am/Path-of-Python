@click.command('init-db')
def init_db_command():
	with app.app_context():
		db.create_all()
		click.echo('Database created successfully')

app.cli.add_command(init_db_command)
