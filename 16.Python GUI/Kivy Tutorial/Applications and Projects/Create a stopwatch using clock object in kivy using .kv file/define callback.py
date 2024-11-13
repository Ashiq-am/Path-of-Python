# define callback
import Clock as Clock


def my_callback(dt):
	pass

# clock.schedule_interval with time specified
Clock.schedule_interval(my_callback, 0.5)

# clock.schedule_once with time specified
Clock.schedule_once(my_callback, 5)

# call my_callback as soon as possible.
Clock.schedule_once(my_callback)
