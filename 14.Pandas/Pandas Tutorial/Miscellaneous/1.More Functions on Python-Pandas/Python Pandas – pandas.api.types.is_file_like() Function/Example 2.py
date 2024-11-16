# import packages
import io
from pandas.api.types import is_file_like

buffer = io.StringIO("geeksforgeeks")
# checking if it's a file like object
print(is_file_like(buffer))
