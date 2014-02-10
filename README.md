Camo Client
===========

[![Build Status](https://travis-ci.org/sionide21/camo-client.png)](https://travis-ci.org/sionide21/camo-client)
[![Latest Version](https://pypip.in/v/camo-client/badge.png)](https://pypi.python.org/pypi/camo-client/)

A python client for Github's [Camo image proxy](https://github.com/atmos/camo).


## Installation

This package is available on pypi. Installation is as simple as:

    pip install camo-client


## Usage

### For individual urls

```python
from camo import CamoClient


client = CamoClient("https://mycamoinstance.com", key="my camo key")
url = client.image_url("http://someothersite.com/path/to/image.png")
```

### For html snippets

```python
from camo import CamoClient


client = CamoClient("https://mycamoinstance.com", key="my camo key")
html = """\
<p>
    Here is a picture:
    <img src="http://someothersite.com/path/to/image.png" alt="It's a banana">
</p>
"""

client.parse_html(html)
```


### For Django

This doesn't directly ship with a django filter but you can simply add the following snippet to you templatetags

```python
from camo import CamoClient
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def proxy_images(text):
    client = CamoClient(settings.CAMO_URL, key=settings.CAMO_KEY)
    return client.parse_html(text)
```


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Ensure the tests pass (`nosetests`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new Pull Request
