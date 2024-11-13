class Config:
	settings = {"mode": "normal", "debug": False}

# Update a key in the dictionary by reference
Config.settings["debug"] = True

# Accessing the updated dictionary
print(Config.settings)
