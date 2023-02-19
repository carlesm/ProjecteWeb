#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple API client, using URLLIB, receiving XML
API:
https://info.arxiv.org/help/api/basics.html

@author: carlesm
'''

import urllib, urllib.request

class ArxivClient(object):
    def __init__(self):
        super(ArxivClient, self).__init__()
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=1&search_query="


    
    def query_arxiv(self, query):
        # connect to URL
        url_query = urllib.request.urlopen(self.url+query)
        # get result
        xml_data = url_query.read().decode("utf-8")
        # handle errors
        return xml_data

    def xml_to_dict(self, results):
        # parxe XML to dict (all at once)
        pass

    def extract_data(self, data):
        # get part of data dict
        pass

    
    def get_data(self, query):
        # query arxiv
        results = self.query_arxiv(query)
        # convert XML to data
        data = self.xml_to_dict(results)
        # trim data
        data = self.extract_data(data)
        # return data
        return data
        


if __name__=="__main__":
    client = ArxivClient()
    data = client.get_data("ltsm")
    print(data)