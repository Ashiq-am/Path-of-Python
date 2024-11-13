# importing module. But will give error. Module not installed
from sqlalchemy_jsonfield import JSONField
Base = declarative_base()


class ExampleModel(Base):
	__tablename__ = 'example_table'
	id = Column(Integer, primary_key=True)
	json_data = Column(JSONField)


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
example_instance = ExampleModel(json_data={'key': 'value'})
with engine.connect() as connection:
	example_instance_id = connection.execute(ExampleModel.__table__.insert(
	).returning(ExampleModel.id, ExampleModel.json_data)).fetchone()
	print(
		f"Inserted ExampleModel with ID: {example_instance_id[0]} and JSON data: {example_instance_id[1]}")
