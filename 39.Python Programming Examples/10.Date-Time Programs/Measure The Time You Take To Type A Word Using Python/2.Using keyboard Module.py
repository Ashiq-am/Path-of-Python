import keyboard
import time

word = "GeeksforGeeks"
typed_word = ""

print(f"Type the word '{word}': ")
start_time = time.time()

while True:
	event = keyboard.read_event(suppress=True)
	if event.event_type == keyboard.KEY_DOWN:
		if event.name == "enter":
			break
		typed_word += event.name

end_time = time.time()
time_taken = end_time - start_time
wpm = len(word) / (time_taken / 60)

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Typing speed: {wpm:.2f} WPM")
