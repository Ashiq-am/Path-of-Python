def _isdst(self, dt):

		tt = (dt.year, dt.month, dt.day,
			dt.hour, dt.minute, dt.second,
			dt.weekday(), 0, 0)

		stamp = _time.mktime(tt)
		tt = _time.localtime(stamp)

		return tt.tm_isdst > 0
