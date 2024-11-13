# import keyboard module.
import keyboard

# pause() function definition.
def pause():
	while True:
		if keyboard.read_key() == 'space':
			# If you put 'space' key
			# the program will resume.
			break


print("GeeksforGeeks printed before pause function")
pause()
print("GeeksforGeeks printed after pause function")
