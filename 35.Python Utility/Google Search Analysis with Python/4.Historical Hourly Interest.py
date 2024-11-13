kw_list = ["Cloud Computing"]
Trending_topics.build_payload(kw_list)
data = Trending_topics.get_historical_interest(
kw_list, year_start=2018, month_start=1, day_start=1,
hour_start=0, year_end=2018, month_end=2, day_end=1,
hour_end=0, cat=0, geo='', gprop='', sleep=0)
data = data.sort_values(by="Cloud Computing", ascending = False)
data = data.head(10)
print(data)
