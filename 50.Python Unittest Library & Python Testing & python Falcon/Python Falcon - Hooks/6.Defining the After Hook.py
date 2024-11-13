def add_custom_header(req, resp, resource, req_succeeded):
    logger.info(f"Processing {req.method} request for {req.path}")
    resp.set_header('X-Custom-Header', 'CustomValue')
