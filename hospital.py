#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

import re
import os
import base64
import sys

import subprocess



def decodePicData():
    picData = '''/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a\nHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy\nMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAoAHgDASIA\nAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA\nAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3\nODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm\np6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA\nAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx\nBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK\nU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3\nuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2iubK\n+JdRJBaKwhPp94j9Tn8q6J3WNGd2CooJZmOAB6mqjajuKC1t5bgucK4G1BxkEseq+6hv5A7tpbnE\ncrqugJBJaRG6muL66l2736Be5xyeMjv611bXcFqUtIVeaVF2iGLlgAB1JOF4I+8RntmubiuU1PW7\ni7uriGGK2gKRyCQqqvgk8hgWwA/IxkLnirckmlwXi2ctjZqqSm5iYKhjiKbhvYhMR4KKNzYO4kA/\nLQ3ZXKUegmq3OqXczWdq/lyh41aOFiMK2/5mY4bb8gwwABOV+bFZRs/EAULPdXYZYgxhSUu55Y7f\nlJGcK+CxAJ2Lnn5ds3LQw2drpM6Tu0aRHy0RoogqvgkIf3e4oV3YZQVxtpus3Nzp2hpJBcBJXlxG\n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'''
    decodeData = base64.b64decode(picData)

    file=open('cache.png','wb')  
    file.write(decodeData)  
    file.close()  

def parsePicData():
    exePath = "C:/Tesseract-OCR/tesseract.exe "
    filePath = sys.path[0] + "/cache.png "
    output_file = "output_file "
    parseLanguage = "-l eng "

    exePath = exePath + filePath + output_file + parseLanguage
    print(exePath)     
    subplaypro = subprocess.Popen(exePath, shell=True)
    subplaypro.wait()


def main():
    """docstring for main"""
    print("main start")
    # createUI()
    parsePicData()

    print("main done")
    
if __name__ == '__main__':
    main()