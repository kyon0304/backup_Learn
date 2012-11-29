#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# file: genThumbnail.py
# date: 2012-11-28 author: kyon

import os, sys
from PIL import Image

def test():
    for i in sys.argv:
        print i,
    print

def generate(infile, width, height, max_bytes=(80*1024)):
    '''
        如果图片小于80K则不进行缩放
        第一个参数：图片路径+图片名
        第二个和第三个参数：图片宽和高
    '''
    length = os.path.getsize(infile)
    if length < max_bytes:
        print "little enough"
        return infile

    size = width, height
    print infile
#    outfile = os.path.splitext(infile)[0]+".thumb"
    outfile = infile.split('.')[0]+'.thumb'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print "cannot create thumbnail for '%s'" % infile
    return outfile

def oneThumb():
    '''
        单个图生成缩略图
    '''
    argc = len(sys.argv)
    filename = sys.argv[1]
    if argc == 2:
        width, heigh = 640, 480
        max_bytes = 80*1024
    elif argc == 4:
        width, height = int(sys.argv[2]), int (sys.argv[3])
        max_bytes = 80*1024
    elif argc == 5:
        width, height = int(sys.argv[2]), int (sys.argv[3])
        max_bytes = int(sys.argv[4])
    else:
        print 'wrong input number!'
        return
    generate(filename, width, height, max_bytes)

def moreThumb():
    width = int(raw_input("Input wanted width:"))
    height = int(raw_input("Input wanted height:"))
    max_bytes = int(raw_input("Input wanted maxbytes:"))
    thumbdir = 'thumb'+'w'+str(width)+'h'+str(height)
    if len(sys.argv)==2 and os.path.isdir(sys.argv[1]):
        '''
            图集--整个文件夹生成缩略图，存放在 文件夹名_thumbwXXhYY 文件夹下
            .jpg的是原图足够小，没有经过缩放.thumb是w为XX, h为YY的缩略图
        '''
        for root, dirs, files in os.walk(sys.argv[1]):
            for name in files:
                fullname = os.path.join(root, name)
                outname = generate(fullname, width, height, max_bytes)
                print name
                fullThumbName = os.path.join(os.path.dirname(outname)+'_'+thumbdir,os.path.basename(outname))
                if not os.path.exists(os.path.dirname(fullThumbName)):
                    os.mkdir(os.path.dirname(fullThumbName))
                os.rename(outname, fullThumbName)
            if '.svn' in dirs:
                dirs.remove('.svn')
    else:
        '''
            图集--多选生成缩略图, 文件名_thumbwXXhYY.thumb
        '''
        for name in sys.argv[1:]:
            outname = generate(name, width, height, max_bytes)
            os.rename(outname, outname.split('.')[0]+'_thumbw'+str(width)+'h'+str(height)+'.thumb')

if __name__ == '__main__':
    moreThumb()
