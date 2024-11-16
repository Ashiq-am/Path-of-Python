import pandas as pd

# creating a dataframe
df = pd.DataFrame({"Team": ["Radisson", "Radisson", "Gladiators",
                            "Blues", "Gladiators", "Blues",
                            "Gladiators", "Gladiators", "Blues",
                            "Blues", "Radisson", "Radisson"],

                   "Position": ["Player", "Extras", "Player", "Extras",
                                "Extras", "Player", "Player", "Player",
                                "Extras", "Player", "Player", "Extras"],

                   "Age": [22, 24, 21, 29, 32, 20, 21, 23, 30, 26, 20, 31]})
df
