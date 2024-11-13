def github_repo(user_name, pass_word,
                repository_name, descriptions=False,
                private=False, readme=False):
    # Open github login page
    driver.get('https://github.com/login')

    # Username
    username = driver.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys(user_name)

    # Password
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys(pass_word)

    # Click on sigin button
    sigin = driver.find_element_by_xpath(
        '//*[@id="login"]/div[4]/form/input[14]')
    sigin.click()

    # Create new repo.
    new_repo = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
    new_repo.click()

    # Enter Repo. name
    repositoryname = driver.find_element_by_xpath('//*[@id="repository_name"]')
    repositoryname.send_keys(repository_name)

    # Optional

    # Enter Description
    if descriptions:
        description = driver.find_element_by_xpath(
            '//*[@id="repository_description"]')
        description.send_keys(descriptions)

    # Private Mode
    if private:
        private = driver.find_element_by_xpath(
            '//*[@id="repository_visibility_private"]')
        private.click()

    # Create ReadMe File
    if readme:
        readme = driver.find_element_by_xpath(
            '//*[@id="repository_auto_init"]')
        readme.click()
