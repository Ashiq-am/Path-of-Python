import time
import os


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main execution block
def main():
    while True:
        current_time_24hr = time.strftime("%H:%M:%S")
        current_time_12hr = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%Y-%m-%d")

        # Clear the screen for a fresh update
        clear_screen()

        print(f"24-Hour Format: {current_time_24hr}")
        print(f"12-Hour Format: {current_time_12hr}")
        print(f"Current Date: {current_date}")

        # Pause for one second between updates
        time.sleep(1)


# Run the clock
if __name__ == "__main__":
    main()
