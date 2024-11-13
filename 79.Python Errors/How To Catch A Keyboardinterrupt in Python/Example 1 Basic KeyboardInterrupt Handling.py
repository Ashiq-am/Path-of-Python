try:
	while True:
		user_input = input("Enter something (Ctrl+C to exit): ")
		print(f"You entered: {user_input}")
except KeyboardInterrupt:
	print("\nProgram terminated by user.")
