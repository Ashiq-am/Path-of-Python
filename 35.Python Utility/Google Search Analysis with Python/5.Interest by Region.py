data = Trending_topics.interest_by_region()
data = data.sort_values(by="Cloud Computing",
						ascending = False)
data = data.head(10)
print(data)
