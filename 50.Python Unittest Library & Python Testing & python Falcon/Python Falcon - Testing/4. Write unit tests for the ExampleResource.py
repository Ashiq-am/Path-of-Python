import unittest
import falcon.testing
from api.app import api


class TestExampleResource(unittest.TestCase):
    def setUp(self):
        self.app = falcon.testing.TestClient(api)

    def test_get_example(self):
        result = self.app.simulate_get('/example')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.text, 'Example GET Response')


if __name__ == '__main__':
    unittest.main()
