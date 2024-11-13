t = Timer(time.process_time)
with t:
	countdown(1000000)
print(t.elapsed)
