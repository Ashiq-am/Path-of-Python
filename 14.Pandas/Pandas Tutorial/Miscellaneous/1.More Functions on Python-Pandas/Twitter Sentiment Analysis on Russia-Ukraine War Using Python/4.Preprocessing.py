# slicing the date , and removing the time portion
tweets['date'] = tweets.date.str.slice(0, 10)
