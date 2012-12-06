#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: handleThumbnails.py
# date: 2012-11-29 author: kyon

import web
import os
import genThumbnail
import ar

urls = ('/thumbnails/', 'thumbnail',
        '/gallery/', 'gallery',
        '/single/', 'single')
BUF_SIZE = 80*1024
class thumbnail:
    def GET(self):
        size = web.input()
        width = int(size['imgWidth'])
        height = int(size['imgHeight'])
        return '[GET]' + str(width) + str(height)

    def POST(self):
        pass

class single:
    def GET(self):
        info = web.input()
        keys = list(info.keys())
        if 'scale' not in keys:
            scale = 'notSpecified'
        else:
            scale = info['scale']
        if 'imgWidth' not in keys or 'imgHeight' not in keys:
            width, height = 0, 0
        else:
            width, height = info['imgWidth'], info['imgHeight']
        folder = os.path.join(ar.DATA_DIR, 'img')
        img = info['image']
        if scale == '':
            scale = 'notSpecified'
        if width == '' or height == '':
            width, height = 0, 0
        if scale == 'notSpecified' and width ==0:
            raise internalerror()
        web.header('Content-type', 'image/%s'%img[img.rfind('.')+1:])
        thumbFile = ar.oneThumb(img, folder, width, height, scale)
        web.debug(thumbFile)
        try:
            f = open(thumbFile, 'rb')
            while True:
                c = f.read(BUF_SIZE)
                if c:
                    yield c
                else:
                    break
        except Exception, e:
            web.debug(e)
            yield 'Error'
        finally:
            if f:
                f.close()
        
    def POST(self):
        pass

class gallery:
    def GET(self):
        info = web.input()
        folder = os.path.join(ar.DATA_DIR+'img/', info['foldername'])
        try:
            isForceRefresh = info['isForceRefresh']
        except:
            isForceRefresh = 'false'
        web.debug("===================start======================")
        if isForceRefresh == 'true':
            urlfile = ar.moreThumb(folder)
        else:
        	urlfile = os.path.join(folder, 'index.json')
        return open(urlfile ,'r').read()

    def POST(self):
        pass

def notfound():
    return web.notfound('Sorry,')
def internalerror():
    return web.internalerror("Bad, you must specify scale or both width and height")

def RunTApp():
    app = web.application(urls, globals())
    app.run()

if __name__ == '__main__':
    RunTApp()
