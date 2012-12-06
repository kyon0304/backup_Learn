#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: genThumbnail.py
# date: 2012-11-28 author: kyon

import os, sys
from PIL import Image
import shutil
import json

MAX_BYTES = 10*1024
SCALE = {
            'notSpecified' : (2,),
            'small' : (1, 480, 480),
            'middle' : (1, 640, 640),
            'large' : (1, 1440, 900)
        }


def generate(infile, width, height, max_bytes=MAX_BYTES):
    '''
        如果图片小于80K则不进行缩放
        第一个参数：图片路径+图片名
        第二个和第三个参数：图片宽和高
    '''
    if os.path.splitext(infile)[-1] in ('.txt', '.json'):
        return "pass|" + infile
    length = os.path.getsize(infile)
    if length < max_bytes:
        print infile, length, "little enough"
        return "origin|" + infile + '|' + infile

    size = width, height
    name, suffix = os.path.splitext(infile)
    outfile = name + '_w' + str(width) + 'h' + str(height) + suffix
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
    return "thumb|" + infile + '|' + outfile

def oneThumb(filename, dirname, width, height, scale, max_bytes = MAX_BYTES):
    '''
        单个图生成缩略图
    '''
    if scale != 'notSpecified':
        width = SCALE[scale][1]
        height = SCALE[scale][2]
    thumbFolder = os.path.join(dirname, 'thumb_'+scale)
    if not os.path.exists(thumbFolder):
        os.mkdir(thumbFolder)

    fullname = os.path.join(dirname, filename)
    thumbFolder = os.path.join(dirname, 'thumb_'+scale)
    thumbFile = os.path.join(thumbFolder, os.path.splitext(filename)[0]+'_w'+str(width)+'h'+str(height)+os.path.splitext(filename)[1])
    if os.path.exists(thumbFile):
        return thumbFile
    outname = generate(fullname, width, height, max_bytes).split('|')
    #print outname
    if outname[0] == 'pass':
        return 'notFound.jpg'
    fullThumbName = os.path.join(thumbFolder, os.path.basename(outname[2]))
    if outname[0] == 'origin':
        shutil.copyfile(outname[1], fullThumbName)
    elif outname[0] == 'thumb':
        os.rename(outname[2], fullThumbName)
    #idxFullThumbName = os.path.join(os.path.sep, fullThumbName)
    #return idxFullThumbName
    return fullThumbName
	
def moreThumb(dirname, max_bytes = MAX_BYTES):
    imgLists = []
    if os.path.isdir(dirname):
        '''
            图集--整个文件夹生成缩略图，文件夹名_thumb 文件夹下
            #存放在 文件夹名_thumbwXXhYY 文件夹下
            .jpg的是原图足够小，没有经过缩放.thumb是w为XX, h为YY的缩略图
        '''
        urlfile = os.path.join(dirname, 'index.json')
        for root, dirs, files in os.walk(dirname):
            for name in files:
                if os.path.splitext(name)[-1] not in ('.txt', '.json'):
                    url = '/single/?image=%s&scale=&imgWidth=&imgHeight=' % name
                    imgLists.append(url)
            del dirs[:]#消除递归，只列第一层文件
        try:
			uf = open(urlfile, 'wr')
			jsonstr = json.dumps(imgLists)
			uf.write(jsonstr)
			uf.close()
        except IOError, TypeError:
			print 'Something goes wrong while open %s' % urlfile
        return urlfile
			
def genIndex(imgLists):
    originfile = os.path.join(os.path.dirname(imgLists[0]),"index.txt")
    try:
        of = open(originfile, 'wr')
        [of.write(i+'|') for i in imgLists]
        of.close()
    except IOError, TypeError:
        print 'something wrong occured while open "%s"' % filename
        print len(imgLists), imgLists

def genJSON(imgLists):
    originfile = os.path.join(os.path.dirname(imgLists[0]), "index.json")
    try:
        of = open(originfile, 'wr')
        jsonstr = json.dumps(imgLists)
        of.write(jsonstr)
        of.close()
    except IOError, TypeError:
        print 'something wrong occured while open "%s"' % filename
        print len(imgLists), imgLists
    

if __name__ == '__main__':
    out = moreThumb('../static/data/img/png', 0, 0, 'middle')
#    out = moreThumb('../img/png', 480, 480)
#    genIndex(out)
    genJSON(out)
    #print out
