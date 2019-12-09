#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
downloader: get_page
"""

import os
import sys
import time

import requests


def get_page(url, proxy_use=True, proxy_reuse=False):
    """
    下载网页
    :param url:    string, url
    :returns: string or None
    """
    response = requests.get(url)
    html = response.text
    return html


def main():
    """
    main function
    """
    home_url = sys.argv[1]
    html = get_page(home_url)
    print("%s" % (html,))

if __name__ == '__main__':
    main()
