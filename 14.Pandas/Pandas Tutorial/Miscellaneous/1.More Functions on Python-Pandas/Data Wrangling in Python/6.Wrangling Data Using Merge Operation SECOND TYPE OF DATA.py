# Import module
import pandas as pd

# Creating Dataframe for Fees_Status
fees_status = pd.DataFrame(
	{'ID': [101, 102, 103, 104, 105,
			106, 107, 108, 109, 110],
	'PENDING': ['5000', '250', 'NIL',
				'9000', '15000', 'NIL',
				'4500', '1800', '250', 'NIL']})

# Printing fees_status
print(fees_status)
