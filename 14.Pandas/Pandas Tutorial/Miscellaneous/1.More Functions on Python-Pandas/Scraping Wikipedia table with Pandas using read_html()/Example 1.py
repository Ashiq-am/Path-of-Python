import pandas as pd

html_string = '''
<table>
<tr>	
	<th>Company</th>
	<th>Contact</th>
	<th>Country</th>
</tr>
<tr>
	<td>Alfreds Futterkiste</td>
	<td>Maria Anders</td>
	<td>Germany</td>
</tr>
<tr>
	<td>Centro comercial Moctezuma</td>
	<td>Francisco Chang</td>
	<td>Mexico</td>
</tr>
</table>
'''
df_1 = pd.read_html(html_string)
df_1
