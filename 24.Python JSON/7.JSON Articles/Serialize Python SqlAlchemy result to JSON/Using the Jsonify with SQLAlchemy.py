from sqlalchemy.ext.declarative import DeclarativeMeta
import json

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Database setup
engine = create_engine('sqlite:///:memory:')  # In-memory database for demonstration
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # Convert SQLAlchemy model to dictionary
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, obj)
# Create sample data
user1 = User(name="John Doe", email="john.doe@example.com")
user2 = User(name="Jane Smith", email="jane.smith@example.com")
session.add_all([user1, user2])
session.commit()
# Serialize a single user
user = session.query(User).first()
user_json = json.dumps(user, cls=AlchemyEncoder)
print(user_json)

# Serialize all users
users = session.query(User).all()
users_json = json.dumps(users, cls=AlchemyEncoder)
print(users_json)
