import tornado.httpclient

async def fetch_data():
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = await http_client.fetch("http://localhost:8001/api")
    print(response.body)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(fetch_data)
