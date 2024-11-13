import time

word = "GeeksforGeeks"

start_time = time.time()
input_word = input(f"Type the word '{word}': ")
end_time = time.time()

time_taken = end_time - start_time
wpm = len(word) / (time_taken / 60)

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Typing speed: {wpm:.2f} WPM")
