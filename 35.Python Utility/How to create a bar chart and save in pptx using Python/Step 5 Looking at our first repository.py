repositories = response_json['items']
first_repo = repositories[0]

print(f"Output \n *** Repository information keys total - {len(first_repo)} - values are -\n")
for keys in sorted(first_repo.keys()):
    print(keys)

print(
    f" *** Repository name - {first_repo['name']}, Owner - {first_repo['owner']['login']}, total watchers - {first_repo['watchers_count']} ")
