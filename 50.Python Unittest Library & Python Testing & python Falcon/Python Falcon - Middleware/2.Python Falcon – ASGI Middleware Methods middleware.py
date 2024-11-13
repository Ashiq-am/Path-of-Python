class SampleASGIMiddleware:
    async def process_request(self, req, resp):
        print("Processing request...")
        # Modify request object if needed

    async def process_response(self, req, resp, resource, req_succeeded):
        print("Processing response...")
        # Modify response object if needed
