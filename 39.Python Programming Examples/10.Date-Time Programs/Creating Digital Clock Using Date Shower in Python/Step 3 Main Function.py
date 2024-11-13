# defining main function
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
