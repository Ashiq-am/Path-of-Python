query = 'geeks for geeks'
choices = ['geek for geek', 'geek geek', 'g. for geeks']

# Get a list of matches ordered by score, default limit to 5
process.extract(query, choices)
[('geeks geeks', 95), ('g. for geeks', 95), ('geek for geek', 93)]

# If we want only the top one
process.extractOne(query, choices)
('geeks geeks', 95)
