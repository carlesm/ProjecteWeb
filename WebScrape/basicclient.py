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

    def get_web_page(self):
        # connect to url
        # get URL content
        # store content
        pass

    def search_html(self):
        # search HTML received for 
        # what we look for
        return None

    def parse_html(self, html):
        # parse found data        
        return None

    def parse_web_page(self):
        # search for data in html
        # extract data from html
        # store data
        html = self.search_html()
        self.data = self.parse_html(html)
        

    def get_data(self):
        # get_web_page
        # parse_web_page
        # return data
        self.get_web_page()
        self.parse_web_page()
        return self.data


if __name__ == "__main__":
    client = WebClient()
    data = client.get_data()
    print(data)