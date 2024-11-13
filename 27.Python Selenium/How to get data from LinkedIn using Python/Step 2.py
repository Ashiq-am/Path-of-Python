options = webdriver.ChromeOptions()
options.add_argument("headless")

exe_path = ChromeDriverManager().install()
service = Service(exe_path)
driver = webdriver.Chrome(service=service, options=options)
