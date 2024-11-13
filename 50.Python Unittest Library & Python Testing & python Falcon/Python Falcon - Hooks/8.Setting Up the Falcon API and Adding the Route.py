app = falcon.App()
app.add_route('/custom', ResourceWithAfterHook())
