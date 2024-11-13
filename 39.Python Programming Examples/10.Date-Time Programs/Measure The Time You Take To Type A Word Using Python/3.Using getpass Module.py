import getpass
import time

word = "GeeksforGeeks"

print(f"Type the word '{word}': ")
start_time = time.time()
typed_word = getpass.getpass(prompt="") # Use getpass for hidden input
end_time = time.time()

time_taken = end_time - start_time
wpm = len(word) / (time_taken / 60)

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Typing speed: {wpm:.2f} WPM")
