# import the module
import pandas as pd

# create a DataFrame
ODI_runs = {'name': ['Tendulkar', 'Sangakkara', 'Ponting',
					'Jayasurya', 'Jayawardene', 'Kohli',
					'Haq', 'Kallis', 'Ganguly', 'Dravid'],
			'runs': [18426, 14234, 13704, 13430, 12650,
					11867, 11739, 11579, 11363, 10889]}
df = pd.DataFrame(ODI_runs)

# making a yellow border
df.style.set_table_styles([{'selector' : '',
							'props' : [('border',
										'10px solid yellow')]}])
