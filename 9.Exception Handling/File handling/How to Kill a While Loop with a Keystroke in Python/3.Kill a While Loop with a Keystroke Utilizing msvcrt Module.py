import msvcrt

def main_loop():
	while True:
		# Your loop logic here
		print("Working...")

		# Check for a key press to break the loop
		if msvcrt.kbhit():
			key = msvcrt.getch().decode()
			if key == 'q':
				print("Loop terminated by user.")
				break

if __name__ == "__main__":
	main_loop()
