# create texttable object
import texttable as tt
table = tt.Texttable()

# Add an empty row at the beginning for the headers
table.add_rows([(None, None, None, None)] + data)

# 'l' denotes left, 'c' denotes center,
# and 'r' denotes right
table.set_cols_align(('c', 'c', 'c', 'c'))
table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))

print(table.draw())
