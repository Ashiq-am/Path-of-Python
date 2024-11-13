# main app class
class Main(MDApp):
	def build(self):
		# returns kv
		return Builder.load_string(KV)

# running app
Main().run()
