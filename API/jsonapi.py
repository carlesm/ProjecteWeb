#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple API client, using requests, receiving JSON
APIs:
https://api.ipify.org/?format=json
https://ipinfo.io/<IP>/geo

@author: carlesm
'''

import requests
import pprint
import sys 
import json


class IPInfo(object):
    def __init__(self):
        super(IPInfo, self).__init__()
        self.url_ip = "https://api.ipify.org/?format=json"
        self.url_info = "https://ipinfo.io/"
        self.url_info_suffix = "/geo"



    
    def get_own_ip(self):
        # query ipify -> JSON
        result = requests.get(self.url_ip)
        # parse result (JSON -> dict)
        data = json.loads(result.text)
        # extract IP
        return data["ip"]
        

    def query_ip_info(self, query):
        # query_ip_info -> JSON
        result = requests.get(self.url_info+query+self.url_info_suffix)
        # parse result (JSON -> dict)
        data = json.loads(result.text)
        # extract info
        return data

    def get_data(self, query=None):
        # if !query
        #   IP = get_own_IP
        if not query:
            data = self.get_own_ip()
        # query ipinfo
        data = self.query_ip_info(data)
        # parse data
        # extract data
        return data



if __name__=="__main__":
    client = IPInfo()
    if len(sys.argv)>1:
        data = client.get_data(sys.argv[1])
    else:
        data = client.get_data()
    pprint.pprint(data)