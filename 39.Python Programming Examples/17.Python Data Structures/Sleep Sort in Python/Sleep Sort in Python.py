import threading
import time

def sleep_sort(numbers):
    def sleep_and_print(n, max_value):
        time.sleep(n * 0.01)  # Scale sleep time down to 1% of the number value
        print(n, end=' ')

    if not numbers:
        return

    max_value = max(numbers)
    threads = []
    for num in numbers:
        thread = threading.Thread(target=sleep_and_print, args=(num, max_value))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Example usage:
arr = [4, 3, 6, 1, 7, 2, 5]
print("Sorted array:", end=' ')
sleep_sort(arr)
print()
