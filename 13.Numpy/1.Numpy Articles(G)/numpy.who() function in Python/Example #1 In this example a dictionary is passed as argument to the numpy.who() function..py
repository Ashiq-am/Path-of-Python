# import the numpy module as np
import numpy as np

# dictionary containing numpy ndarrays
gfg = {'arr_1': np.arange(3), 'arr_2': np.arange(6),
	'name': 'some text', 'number': 34523}

# passing the dict as argument
np.who(gfg)
