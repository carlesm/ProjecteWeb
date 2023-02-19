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
import xmltodict
import pprint
import sys 


class ArxivClient(object):
    def __init__(self):
        super(ArxivClient, self).__init__()
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=2&search_query="


    
    def query_arxiv(self, query):
        # connect to URL
        url_query = urllib.request.urlopen(self.url+query)
        # get result
        xml_data = url_query.read().decode("utf-8")
        # handle errors
        return xml_data

    def xml_to_dict(self, results):
        # parxe XML to dict (all at once)
        results = xmltodict.parse(results)
        return results

    def extract_data(self, data_in):
        data = []
        for e in data_in["feed"]["entry"]:
            title = e["title"]
            authors = "'".join([a["name"] for a in e["author"]])
            data.append((title, authors))
        # get part of data dict
        return data

    
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
    if len(sys.argv)>1:
        data = client.get_data(sys.argv[1])
    else:
        data = client.get_data("ltsm")
    pprint.pprint(data)