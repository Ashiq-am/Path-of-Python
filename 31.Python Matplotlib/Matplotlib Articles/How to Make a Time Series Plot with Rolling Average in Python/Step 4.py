# computing a 7 day rolling average
data[ '7day_rolling_avg' ] = data.Births.rolling( 7).mean()

# viewing the dataset
Display(data.head(10))
