from sqlalchemy import ForeignKey

address_table = Table(
	"address",
	metadata_object,
	Column('id', Integer, primary_key=True),
	Column('student_id', ForeignKey('student_account.id'), nullable=False),
	Column('email_address', String, nullable=False)
)
