#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB and basic parsing

@author: carlesm
'''


class WebClient(object):

    def __init__(self) -> None:
        super(WebClient, self).__init__()
        self.data = None

    def get_web_page():
        # connect to url
        # get URL content
        # store content
        pass

    def parse_web_page():
        # search for data in html
        # extract data from html
        # store data
        pass

    def get_data():
        # get_web_page
        # parse_web_page
        # return data

        pass


if __name__ == "__main__":
    client = WebClient()
    data = client.get_data()
    print(data)