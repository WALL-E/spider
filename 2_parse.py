#!/usr/bin/env python3
# coding:utf-8
"""
从Html文件中解析车辆信息
"""


import sys
import os
import json

from bs4 import BeautifulSoup

def parse_html(html):
    """
    parse html of https://vincar.cn/
    :param html: html strings
    :returns: list
    """
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for i in soup.find_all('a', {"class": "aa"}):
        results.append(i.attrs["href"])
    return results


def main():
    """
    main function
    """
    if len(sys.argv) < 2:
        print("%s filename.html" % (sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print("%s is not exists" % (filename))
        sys.exit(1)
    html = open(filename).readlines()
    data = parse_html("".join(html))
    for i in data:
        print("%s%s" % ("http://dycg.dongying.gov.cn", i))


if __name__ == "__main__":
    main()
