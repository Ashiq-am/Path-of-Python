from sqlalchemy import create_engine
from sqlalchemy import DateTime, Numeric, Enum

item_detail = Table(
	"items",
	metadata_object,
	Column("key", String(50), primary_key=True),
	Column("timestamp", DateTime),
	Column("price", Numeric(100, 2)),
	Column("type", Enum("dry", "wet")),
)

# createing an engine object
engine = create_engine("sqlite+pysqlite:///:memory:",
					echo=True, future=True)

# emitting DDL
metadata_object.create_all(engine)
