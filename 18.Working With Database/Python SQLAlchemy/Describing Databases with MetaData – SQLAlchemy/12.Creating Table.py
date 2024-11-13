from sqlalchemy import create_engine

# createing an engine object
engine = create_engine("sqlite+pysqlite:///:memory:",
					echo=True, future=True)
# emitting DDL
metadata_object.create_all(engine)
