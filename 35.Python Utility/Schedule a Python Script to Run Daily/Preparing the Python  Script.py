# Modules which need to be imported
import webbrowser

# Site which you want to Open in your
# Browser
url = "mail.google.com"

# Below code is used to specify
# location of webbrowser which you
# want to use.
chrome_path = r'C: \Program Files(x86)\Google\Chrome\Application\chrome.exe'

# Below code will open your URL
webbrowser.register(
'chrome', None, webbrowser.BackgroundBrowser(chrome_path))

webbrowser.get('chrome').open_new_tab(url)
