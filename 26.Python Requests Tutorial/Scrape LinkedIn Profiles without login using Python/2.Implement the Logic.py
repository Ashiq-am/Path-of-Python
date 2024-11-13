def scrape_linkedin_profiles(url):
	headers = {
		"User-Agent": "Guest", # Access as Guest
	}

	response = requests.get(url, headers=headers)

	if response.status_code == 200: # if request granted
		soup = BeautifulSoup(response.content, 'html.parser')

		# Extract profile information
		title_tag = soup.find('title')
		designation_tag = soup.find('h2')
		followers_tag = soup.find('meta', {"property": "og:description"})
		description_tag = soup.find('p', class_='break-words')

		# Check if the tags are found before calling get_text()
		name = title_tag.get_text(strip=True).split("|")[0].strip() if title_tag else "Profile Name not found"
		designation = designation_tag.get_text(strip=True) if designation_tag else "Designation not found"

		# Use regular expression to extract followers and description count
		followers_match = re.search(r'\b(\d[\d,.]*)\s+followers\b', followers_tag["content"]) if followers_tag else None
		followers_count = followers_match.group(1) if followers_match else "Followers count not found"

		description = description_tag.get_text(strip=True) if description_tag else "Description not found"

		print(f"Profile Name: {name}")
		print(f"Designation: {designation}")
		print(f"Followers Count: {followers_count}")
		print(f"Description: {description}")
	else:
		print(f"Error: Unable to retrieve the LinkedIn company profile. Status code: {response.status_code}")
