#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

import re

def getBingPicLinks():
    htmlUrl = "https://bing.ioliu.cn"
    try:
        html = urlopen(htmlUrl)
    except (HTTPError, URLError) as e:
        return None
    
    try:
        # print(html.read();
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        # print(bsObj.prettify())
        links = []
        for link in bsObj.find_all(href=re.compile("force=download")):
            downloadLink = htmlUrl + link.get('href')
            print(downloadLink)
            links.append(downloadLink)

    except AttributeError as e:
        return None

    return links


def download_pics(pic_links):
    for link in pic_links:
        localPath = "E:/bingPics/"
        file_name = link.split('/')[-1]

        file_name = file_name.split('?')[0]
        
        print("Downloading file:%s" % file_name)
        localPath = localPath + file_name + ".jpg"
        urlretrieve(link, localPath)
        print("%s downloaded!\n" % file_name)

    print("All Pics downloaded!")

    return

def main():
    """docstring for main"""
    # createUI()
    downloadLinks = getBingPicLinks()
    download_pics(downloadLinks)
    print("main done")
    
if __name__ == '__main__':
    main()