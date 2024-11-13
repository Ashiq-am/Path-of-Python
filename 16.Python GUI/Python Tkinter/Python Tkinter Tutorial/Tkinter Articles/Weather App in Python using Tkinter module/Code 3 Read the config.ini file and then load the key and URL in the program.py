# extract key from the
# configuration file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
