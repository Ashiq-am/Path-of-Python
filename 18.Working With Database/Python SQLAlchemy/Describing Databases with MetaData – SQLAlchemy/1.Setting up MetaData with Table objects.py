from sqlalchemy import MetaData
from sqlalchemy import Integer, String, Column, Table

metadata_object=MetaData()

student_table = Table(
	"student_account",
	metadata_object,
	Column('id', Integer, primary_key=True),
	Column('name', String(30)),
	Column('age',Integer),
	Column('grade', String(80))
)
