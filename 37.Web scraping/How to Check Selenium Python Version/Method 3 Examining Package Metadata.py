import pkg_resources
selenium_version = pkg_resources.get_distribution("selenium").version
print("Selenium version:", selenium_version)
