#!/usr/bin/python 
# -*- coding: utf-8 -*-

class RequestData():

	def __init__(self):
		self.method = None
		self.url = None
		self.host = None
		self.headers = {}
		self.files = {}
		self.data = None
		self.description = None
		self.content_type = None
