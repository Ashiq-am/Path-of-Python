# Import the class
from itemloaders.processors import SelectJmes

# prepare object of SelectJmes
proc = SelectJmes("hello")

# Print the output of json path
print(proc({'hello': 'scrapy'}))
