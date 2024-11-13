# imports
import requests
from plotly.graph_objs import Bar
from plotly import offline

# siteurl and headers
site_url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

# response and parsing the response.
response = requests.get(site_url, headers=headers)
response_json = response.json()

repositories = response_json['items']

# loop the repositories
repo_names, repo_stars = [], []
for repo_info in repositories:
	repo_names.append(repo_info['name'])
	repo_stars.append(repo_info['stargazers_count'])

# graph plotting
data_plots = [{'type' : 'bar', 'x':repo_names , 'y': repo_stars}]
layout = {'title': 'GItHubs Most Popular Javascript Projects',
		'xaxis': {'title': 'Repository'},
		'yaxis': {'title': 'Stars'}}

# saving graph to a Most_Popular_JavaScript_Repos.png
fig = {'data': data_plots, 'layout': layout}
offline.plot(fig, image = 'png', image_filename='Most_Popular_JavaScript_Repos')
