#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: handleThumbnails.py
# date: 2012-11-29 author: kyon

import web
import genThumbnail

urls = ('/thumbnails/','thumbnail')

class thumbnail:
    def GET(self):
        size = web.input()
        width = int(size['imgWidth'])
        height = int(size['imgHeight'])
        return '[GET]' + str(width) + str(height)

    def POST(self):
        pass

def RunApp():
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    RunApp()
