# -*- coding: utf-8 -*-
import json
import codecs

__author__ = 'Daniel'


class Codec(object):
    def decode(self, jsn):
        return json.dumps(jsn, ensure_ascii=False, encoding='utf-8')

    def write(self, jsn, filename):
        with codecs.open(filename, "w", encoding="utf-8") as file:
            file.write(jsn)