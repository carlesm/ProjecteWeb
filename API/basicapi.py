#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple API client, using URLLIB, receiving XML
API:
https://info.arxiv.org/help/api/basics.html

@author: carlesm
'''

class ArxivClient(object):
    def def __init__(self):
        super(ArxivClient, self).__init__()
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=1&search_query="

    
    def get_data(self, query):
        # query arxiv
        # convert XML to data
        # trim data
        # return data
        pass    



if __name__=="__main__":
    client = ArxivClient()
    data = client.get_data("ltsm")
    print(data)