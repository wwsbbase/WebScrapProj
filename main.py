#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError

import re
import os

pages = []
homepageUrl = "https://bing.ioliu.cn"

def getPageLinks(pageUrl):
    # 遍历当前页面链接
    getBingPicLinks(homepageUrl + pageUrl)

    # 获取并进入下一节点
    try:
        html = urlopen(homepageUrl + pageUrl)
    except (HTTPError, URLError) as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        for link in bsObj.find_all(href=re.compile("/?p=")):
            pagelink = link.get('href')
            if pagelink not in pages:
                print("Add new page: " + pagelink)
                pages.append(pagelink)
                getPageLinks(pagelink)

    except AttributeError as e:
        return None

def getBingPicLinks(htmlUrl):
    downloadLinks = []

    # htmlUrl = homepageUrl + page
    print(htmlUrl) 
    try:
        html = urlopen(htmlUrl)
    except (HTTPError, URLError) as e:
        return None
    
    try:
        # print(html.read();
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        # print(bsObj.prettify())
        for link in bsObj.find_all(href=re.compile("force=download")):
            downloadLink = homepageUrl + link.get('href')
            print(downloadLink)
            downloadLinks.append(downloadLink)

    except AttributeError as e:
        return None

    # return links
    download_pics(downloadLinks)

def download_pics(pic_links):
    for link in pic_links:
        localPath = "E:/bingPics/"
        if not os.path.exists(localPath) :
            os.makedirs(localPath)

        file_name = link.split('/')[-1]

        file_name = file_name.split('?')[0]
        
        print("Downloading file:%s" % file_name)
        localPath = localPath + file_name + ".jpg"
        if not os.path.isfile(localPath) :
            urlretrieve(link, localPath)
            print("%s downloaded!\n" % file_name)

    print("All Pics downloaded!")

    return

def main():
    """docstring for main"""
    print("main start")
    # createUI()
    getPageLinks("")

    print("main done")
    
if __name__ == '__main__':
    main()