from dataclasses import dataclass


@dataclass
class Transaction:
	sender: str
	receiver: str
	date: str
	amount: float


# Creating object
record = Transaction(sender="Aryaman",
					receiver="Ankur",
					date="2020-06-18",
					amount=1.0)

print(record)
print(record.receiver)
