# generate median line
median_line = base.mark_rule().encode(
	x=alt.X('mean(height):Q', title='Height'), size=alt.value(5))
