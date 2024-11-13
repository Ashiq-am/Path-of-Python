class Base(DeclarativeBase):
	pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
