# The dataset consists of tweets from
# total 8 hashtags and present in
# separated csv files. All those csv files are loaded.
tweets=pd.read_csv("/dataset/Russia_invade.csv")
tweets=tweets.append(pd.read_csv("/Russian_border_Ukraine.csv"))
tweets=tweets.append(pd.read_csv("/Russian_troops.csv"))
tweets=tweets.append(pd.read_csv("/StandWithUkraine.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_border.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_nato.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_troops.csv"))
tweets=tweets.append(pd.read_csv("/Ukraine_war.csv"))
