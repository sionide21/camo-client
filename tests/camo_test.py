import unittest
from camo import CamoClient, Image


class CamoImageTest(unittest.TestCase):
    def test_encodes_url(self):
        image = Image("http://example.net/images/hahafunny.jpg", key="hello")
        self.assertEqual(image.path, '/735030fa488e1866b4302ac611c075d541a773e3/687474703a2f2f6578616d706c652e6e65742f696d616765732f6861686166756e6e792e6a7067')


class CamoClientTest(unittest.TestCase):
    def test_client(self):
        client = CamoClient("https://fakecdn.org", key="hello")
        self.assertEqual(
            client.image_url("http://example.net/images/hahafunny.jpg"),
            'https://fakecdn.org/735030fa488e1866b4302ac611c075d541a773e3/687474703a2f2f6578616d706c652e6e65742f696d616765732f6861686166756e6e792e6a7067'
        )

    def test_trailing_slash(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        self.assertEqual(
            client.image_url("http://example.net/images/hahafunny.jpg"),
            'https://fakecdn.org/735030fa488e1866b4302ac611c075d541a773e3/687474703a2f2f6578616d706c652e6e65742f696d616765732f6861686166756e6e792e6a7067'
        )
