Camo Client
===========

[![Build Status](https://travis-ci.org/sionide21/camo-client.png)](https://travis-ci.org/sionide21/camo-client)
[![Latest Version](https://pypip.in/v/camo-client/badge.png)](https://pypi.python.org/pypi/camo-client/)

A python client for Github's [Camo image proxy](https://github.com/atmos/camo).


## Installation

This package is available on pypi. Installation is as simple as:

    pip install camo-client


## Usage

```python
from camo import CamoClient


client = CamoClient("https://mycamoinstance.com", key="my camo key")
url = client.image_url("http://someothersite.com/path/to/image.png")
```


## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Ensure the tests pass (`nosetests`)
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new Pull Request
