import collections

Transaction = collections.namedtuple('Transaction',
									['sender', 'amount',
									'receiver', 'date'])

# Creating object
record = Transaction(sender="Aryaman",
					receiver="Ankur",
					date="2020-06-18",
					amount=1.0)

print(record)
print(record.receiver)
