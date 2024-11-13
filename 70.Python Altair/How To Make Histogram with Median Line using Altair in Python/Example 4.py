# generate histogram
hist = base.mark_bar().encode(
	x=alt.X('height:Q', bin=alt.BinParams(), axis=None), y='count()')
