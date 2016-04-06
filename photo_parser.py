#!/usr/bin/python

import sys
import re
import requests

from lxml import etree
from StringIO import StringIO

if not len(sys.argv) > 1:
    print "Usage: ./photo_parser.py <instagram link>"
else:
    response = requests.get(sys.argv[1])

    parser = etree.HTMLParser()
    html = etree.parse(StringIO(response.text), parser)
    result = html.xpath("//meta[@property='og:image']")[0].attrib.get("content")

    print re.sub(r"\?.*", "", result)
