# Getting the HTML of the Experience section in the profile
experience = soup.find("section", {"id": "experience-section"}).find('ul')

print(experience)
