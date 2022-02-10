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

    def test_parses_html(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        html = """<img src="http://example.net/images/hahafunny.jpg" /><img src="https://otherexample/moreserious.png" />"""
        parsed = """<img src="https://fakecdn.org/735030fa488e1866b4302ac611c075d541a773e3/687474703a2f2f6578616d706c652e6e65742f696d616765732f6861686166756e6e792e6a7067">"""\
                 """<img src="https://fakecdn.org/c81915f5756fad02cfae7d07e359624dae877667/68747470733a2f2f6f746865726578616d706c652f6d6f7265736572696f75732e706e67">"""
        self.assertEqual(client.parse_html(html), parsed)

    def test_ignores_already_hosted(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        html = """<p><img src="https://fakecdn.org/images/hahafunny.jpg"></p>"""
        self.assertEqual(client.parse_html(html), html)

    def test_ignores_relative(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        html = """<p><img src="/images/hahafunny.jpg"></p>"""
        self.assertEqual(client.parse_html(html), html)

    def test_unmarkedup_text(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        text = """butts"""
        self.assertEqual(client.parse_html(text), text)
