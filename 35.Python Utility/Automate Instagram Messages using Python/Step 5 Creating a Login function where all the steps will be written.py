def login(self):
    self.bot.get(self.base_url)

    # ENTERING THE USERNAME FOR LOGIN INTO INSTAGRAM
    enter_username = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'username')))

    enter_username.send_keys(self.username)

    # ENTERING THE PASSWORD FOR LOGIN INTO INSTAGRAM
    enter_password = WebDriverWait(self.bot, 20).until(
        expected_conditions.presence_of_element_located((By.NAME, 'password')))
    enter_password.send_keys(self.password)

    # RETURNING THE PASSWORD and login into the account
    enter_password.send_keys(Keys.RETURN)
    time.sleep(5)
