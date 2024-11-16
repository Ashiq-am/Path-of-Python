raw_data = {"first_name": ["Jason", "Molly", "Tina", "Jake", "Amy"],
			"last_name": ["Miller", "Jacobson", "Ali", "Milner", "Cooze"],
			"email": ["jas203@gmail.com", "momomolly@gmail.com", np.NAN,
					"battler@milner.com", "Ames1234@yahoo.com"]}

df = pd.DataFrame(raw_data, columns=["first_name", "last_name", "email"])
print()
print(df)
