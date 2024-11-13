from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import json

# Use the updated import for declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    addresses = relationship("Address", back_populates="user")

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String)
    city = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")

# Create an in-memory SQLite database and set up the session
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Adding example data
user1 = User(name="John Doe", email="john.doe@example.com")
user2 = User(name="Jane Smith", email="jane.smith@example.com")
session.add_all([user1, user2])
session.commit()

address = Address(street="123 Main St", city="Anytown", user=user1)
session.add(address)
session.commit()

def serialize_complex(result):
    if isinstance(result, list):
        return [serialize_complex_single(item) for item in result]
    else:
        return serialize_complex_single(result)

def serialize_complex_single(result):
    data = {c.name: getattr(result, c.name) for c in result.__table__.columns}
    # Add relationships
    if hasattr(result, 'addresses'):
        data['addresses'] = [serialize_complex_single(addr) for addr in result.addresses]
    return data

# Serialize user with addresses
user = session.query(User).first()
user_json = json.dumps(serialize_complex(user), indent=4)
print(user_json)
