# Example lists
team_a = ["Alice", "Bob"]
team_b = ["Charlie", "David"]

# Unpack both lists using starred expressions
*combined_team, captain_b = team_a, *team_b

# Print the results
print("Combined Team:", combined_team)
print("Captain of Team B:", captain_b)
