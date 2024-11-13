class bot:

    def __init__(self, username, password, audience, message):
        # initializing the username
        self.username = username

        # initializing the password
        self.password = password

        # passing the list of user or initializing
        self.user = user

        # passing the message of user or initializing
        self.message = message

        # initializing the base url.
        self.base_url = 'https://www.instagram.com/'

        # here it calls the driver to open chrome web browser.
        self.bot = driver

        # initializing the login function we will create
        self.login()
