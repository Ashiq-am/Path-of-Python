result = set(chain.from_iterable(
		values for key, values in rev_dict.items()
		if len(values) > 1))
