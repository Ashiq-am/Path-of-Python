import chart_studio
username = 'your username'
api_key = 'your api key'

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

py.plot(fig, filename='your filename', auto_open=False, sharing='public')
