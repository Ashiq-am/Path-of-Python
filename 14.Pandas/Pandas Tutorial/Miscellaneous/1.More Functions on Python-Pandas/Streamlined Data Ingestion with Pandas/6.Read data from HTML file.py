# Import the Pandas library
import pandas


# Variable containing the elements
# between <table> tag from webpage
html_string = """
<table>
<thead>
	<tr>
	<th>Date</th>
	<th>Empname</th>
	<th>Year</th>
	<th>Rating</th>
	<th>Region</th>
	</tr>
</thead>
<tbody>
	<tr>
	<td>2020-01-01</td>
	<td>Savio</td>
	<td>2004</td>
	<td>0.5</td>
	<td>South</td>
	</tr>
	<tr>
	<td>2020-01-02</td>
	<td>Rahul</td>
	<td>1998</td>
	<td>1.34</td>
	<td>East</td>
	</tr>
	<tr>
	<td>2020-01-03</td>
	<td>Tina</td>
	<td>1988</td>
	<td>1.00023</td>
	<td>West</td>
	</tr>
	<tr>
	<td>2021-01-03</td>
	<td>Sonia</td>
	<td>2001</td>
	<td>2.23</td>
	<td>North</td>
	</tr>
	<tr>
	<td>2008-01-03</td>
	<td>Milo</td>
	<td>2008</td>
	<td>3.23</td>
	<td>East</td>
	</tr>
	<tr>
	<td>2006-01-03</td>
	<td>Edward</td>
	<td>2005</td>
	<td>0.43</td>
	<td>West</td>
	</tr>
</tbody>
</table>"""

# Pass the string containing html table element
df = pandas.read_html(html_string)

# Since read_html, returns a list object,
# extract first element of the list
dfHtml = df[0]

# Print the data frame object
print(dfHtml)
