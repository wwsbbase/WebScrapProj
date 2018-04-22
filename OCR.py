#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re
import os
import base64
import sys

import subprocess
from PIL import Image
import pytesseract


def parsePicData():
    words = pytesseract.image_to_string(Image.open("cache.png"), lang='eng')
    print(words)
    print("parsePicData")

def testImage():
    im= Image.open("cache.png")
    print(im)
    print(im.format,im.size,im.mode)


def main():
    """docstring for main"""
    print("main start")
    # createUI()
    parsePicData()

    print("main done")
    
if __name__ == '__main__':
    main()