#!pip install pydantic

# Writing the .env file
with open('.env', 'w') as f:
    f.write('db_url=your_database_url\n')
    f.write('api_key=your_api_key\n')

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url: str
    api_key: str


# Load settings from the .env file
settings = Settings(_env_file='.env')

# Print the settings
print(settings.db_url)
print(settings.api_key)
