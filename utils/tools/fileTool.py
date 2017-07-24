# -*- coding: utf8 -*-
import os


def walkDir(_rootdir):
    for parent, dirnames, filenames in os.walk(_rootdir):
        # case 1:
        for dirname in dirnames:
            print("parent folder is:" + parent)
            print("dirname is:" + dirname)
        # case 2
        for filename in filenames:
            print("file name is:" + filename)
            print("parent folder is:" + parent)
            print("filename with full path:" + os.path.join(parent, filename))


rootdir = "E:\测试文件"

walkDir(rootdir)
