import hashlib
import hmac
import re
from memoize import mproperty
from lxml import html


class CamoClient(object):
    def __init__(self, server, key):
        self.server = re.sub('/+$', '', server)
        self.key = key

    def image_url(self, url):
        # skip images that have already been proxied and
        # images with data URIs
        if url.startswith(self.server) or url.startswith("data:image/"):
            return url
        else:
            return self.server + Image(url, self.key).path

    def _rewrite_image_urls(self, node):
        for img in node.xpath('.//img'):
            if img.get('src'):
                img.set('src', self.image_url(img.get('src')))
        return node

    def parse_html(self, string):
        doc = html.fromstring(string.join(['<div>', '</div>']))
        doc = self._rewrite_image_urls(doc)
        # iterating over a node returns all the tags within that node
        # ..if there are none, return the original string
        return ''.join(map(html.tostring, doc)) or string


class Image(object):
    def __init__(self, url, key):
        self.url = url
        self.key = key

    @mproperty
    def path(self):
        return "/%s/%s" % (self.digest, self.encoded_url)

    @mproperty
    def digest(self):
        return hmac.new(self.key, self.url, hashlib.sha1).hexdigest()

    @mproperty
    def encoded_url(self):
        return self.url.encode("hex")
