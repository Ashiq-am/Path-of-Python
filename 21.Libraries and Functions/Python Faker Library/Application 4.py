from faker import Faker
fake = Faker()

fake.seed(1)
print(fake.name())
print(fake.address())
print(fake.email())
