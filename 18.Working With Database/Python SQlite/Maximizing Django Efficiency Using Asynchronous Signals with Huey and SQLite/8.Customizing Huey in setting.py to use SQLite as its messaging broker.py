#settings.py
from huey import SqliteHuey

HUEY = {
    'huey_class': 'huey.SqliteHuey',  # Use the SqliteHuey class
    'name': 'user-huey-app',  # Change to desired name
    'results': True,  # Enable result storage
    'store_none': False,  # If a task returns None, do not save
    'immediate': False,  # If DEBUG=True, run synchronously
    'utc': True,
    'filename': 'huey.sqlite3',  #
}
