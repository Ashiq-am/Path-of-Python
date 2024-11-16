# Removing RT, Punctuation etc
def remove_rt(x): return re.sub('RT @\w+: ', " ", x)

def rt(x): return re.sub(
	"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x)

tweets["content"] = tweets.content.map(remove_rt).map(rt)
tweets["content"] = tweets.content.str.lower()
