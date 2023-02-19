#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple API client, using URLLIB, receiving XML
API:
https://info.arxiv.org/help/api/basics.html

@author: carlesm
'''





if __name__=="__main__":
    client = ArxivClient()
    data = client.get_data()
    print(data)