import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# Function to send notifications
def send_notification(title, message):
	notification.notify(
		title=title,
		message=message,
		timeout=10 # Notification will disappear after 10 seconds
	)

# Function to parse HTML and check for changes
def parse_html(url, last_content):
	try:
		# Send HTTP request and get the webpage content
		response = requests.get(url)
		soup = BeautifulSoup(response.text, 'html.parser')

		# Customize this part based on the structure of the webpage
		current_content = str(soup.find('div', class_='content').text)

		# Check if content has changed since the last check
		if current_content != last_content:
			send_notification("Web Crawler Notification", "New content detected on the webpage!")

		return current_content

	except Exception as e:
		print(f"Error: {e}")
		return last_content

# Main loop to run the script continuously
def main():
	url = "https://www.apple.com/iphone/" # or any example url
	last_content = ""

	while True:
		last_content = parse_html(url, last_content)
		time.sleep(3600) # Check for changes every hour

if __name__ == "__main__":
	main()
