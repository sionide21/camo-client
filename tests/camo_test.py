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
        html = """<img src="http://example.net/images/hahafunny.jpg" /><img src="https://otherexample/moreserious.png" />"""\
               """<img src="//example.net/no_http.jpg" /><img src=" http://example.net/leading_space.jpg" />"""\
               """<img src=http://example.net/mising_quotes.jpg /><img src="ftp://example.net/ftp_image.jpg" />"""\
               """<img src="/images/hahafunny.jpg">"""
        parsed = """<img src="https://fakecdn.org/735030fa488e1866b4302ac611c075d541a773e3/687474703a2f2f6578616d706c652e6e65742f696d616765732f6861686166756e6e792e6a7067">"""\
                 """<img src="https://fakecdn.org/c81915f5756fad02cfae7d07e359624dae877667/68747470733a2f2f6f746865726578616d706c652f6d6f7265736572696f75732e706e67">"""\
                 """<img src="https://fakecdn.org/1d5de168888358e62b7c2f850265c5bfb43e46c3/2f2f6578616d706c652e6e65742f6e6f5f687474702e6a7067">"""\
                 """<img src="https://fakecdn.org/f4837f9cd17f391dd4c78e49f7b57934f6966f7c/20687474703a2f2f6578616d706c652e6e65742f6c656164696e675f73706163652e6a7067">"""\
                 """<img src="https://fakecdn.org/d4ef06afe02debfdcbce1b1b078666e918732793/687474703a2f2f6578616d706c652e6e65742f6d6973696e675f71756f7465732e6a7067">"""\
                 """<img src="https://fakecdn.org/46bb6a3963ac29bd9c1587f2f533dad926c82330/6674703a2f2f6578616d706c652e6e65742f6674705f696d6167652e6a7067">"""\
                 """<img src="https://fakecdn.org/17c855d7008b1307d277d725cb045b0fc0e23ea7/2f696d616765732f6861686166756e6e792e6a7067">"""
        self.assertEqual(client.parse_html(html), parsed)

    def test_ignores_already_hosted(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        html = """<p><img src="https://fakecdn.org/images/hahafunny.jpg"></p>"""
        self.assertEqual(client.parse_html(html), html)

    def test_ignores_data_uri(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        html = """<p><img src="data:image/png;base64,iVBOR0t8XDY0bb"></p>"""
        self.assertEqual(client.parse_html(html), html)

    def test_unmarkedup_text(self):
        client = CamoClient("https://fakecdn.org/", key="hello")
        text = """butts"""
        self.assertEqual(client.parse_html(text), text)
