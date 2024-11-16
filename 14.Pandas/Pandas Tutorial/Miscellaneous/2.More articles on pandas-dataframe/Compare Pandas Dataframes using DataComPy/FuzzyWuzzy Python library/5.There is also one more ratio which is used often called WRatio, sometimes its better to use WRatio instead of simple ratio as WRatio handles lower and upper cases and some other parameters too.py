fuzz.WRatio('geeks for geeks', 'Geeks For Geeks')
100
fuzz.WRatio('geeks for geeks!!!','geeks for geeks')
100
# whereas simple ratio will give for above case
fuzz.ratio('geeks for geeks!!!','geeks for geeks')
91
