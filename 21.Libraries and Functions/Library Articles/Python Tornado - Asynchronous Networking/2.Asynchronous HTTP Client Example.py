import tornado.ioloop
import tornado.httpclient


async def fetch_url(url):
    http_client = tornado.httpclient.AsyncHTTPClient()
    response = await http_client.fetch(url)
    print(response.body)

if __name__ == "__main__":
    tornado.ioloop.IOLoop.current().run_sync(
        lambda: fetch_url("https://example.com"))
