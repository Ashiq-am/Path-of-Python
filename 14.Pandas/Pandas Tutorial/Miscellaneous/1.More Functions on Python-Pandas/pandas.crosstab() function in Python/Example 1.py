# importing packages
import pandas
import numpy

# creating some data
a = numpy.array(["foo", "foo", "foo", "foo",
				"bar", "bar", "bar", "bar",
				"foo", "foo", "foo"],
				dtype=object)

b = numpy.array(["one", "one", "one", "two",
				"one", "one", "one", "two",
				"two", "two", "one"],
				dtype=object)

c = numpy.array(["dull", "dull", "shiny",
				"dull", "dull", "shiny",
				"shiny", "dull", "shiny",
				"shiny", "shiny"],
				dtype=object)

# form the cross tab
pandas.crosstab(a, [b, c], rownames=['a'], colnames=['b', 'c'])
