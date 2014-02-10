import hashlib
import hmac
import re
from memoize import mproperty


class CamoClient(object):
    def __init__(self, server, key):
        self.server = re.sub('/+$', '', server)
        self.key = key

    def image_url(self, url):
        return self.server + Image(url, self.key).path


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
