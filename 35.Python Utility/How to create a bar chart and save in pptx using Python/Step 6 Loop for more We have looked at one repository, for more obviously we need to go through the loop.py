for repo_info in repositories:
	print(f"\n *** Repository Name: {repo_info['name']}")
	print(f" *** Repository Owner: {repo_info['owner']['login']}")
	print(f" *** Repository Description: {repo_info['description']}")
