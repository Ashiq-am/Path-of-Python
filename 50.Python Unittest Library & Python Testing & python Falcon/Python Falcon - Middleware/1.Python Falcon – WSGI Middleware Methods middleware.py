class SampleWSGIMiddleware:
    def process_request(self, req, resp):
        print("Processing request...")
        # Modify request object if needed

    def process_resource(self, req, resp, resource, params):
        print("Processing resource...")
        # Modify request and response objects if needed

    def process_response(self, req, resp, resource, req_succeeded):
        print("Processing response...")
        # Modify response object if needed
