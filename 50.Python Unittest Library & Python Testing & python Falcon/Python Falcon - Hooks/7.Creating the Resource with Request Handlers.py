class ResourceWithAfterHook:
    @falcon.after(add_custom_header)
    def on_get(self, req, resp):
        logger.info("Handling GET request")
        resp.media = {'message': 'Response with a custom header!'}

    @falcon.after(add_custom_header)
    def on_post(self, req, resp):
        logger.info("Handling POST request")
        resp.media = {'message': 'Data received with a custom header!'}
