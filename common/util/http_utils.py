#!/usr/bin/python 
# -*- coding: utf-8 -*-
import decimal
import json
import requests

from common.util.logger import log
from common.util.request_data import *
from common.enums.request_method_enum import *

class DecimalEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, decimal.Decimal):
                return float(o)
            super(DecimalEncoder, self).default(o)

class HttpUtils():
	def __init__(self):
		self.timeout = None

	@classmethod
	def http_request(cls, req_data):
		try:
			request_url = req_data.url
			request_method = req_data.method
			request_headers = req_data.headers
			request_content_type = req_data.content_type
			request_files = req_data.files
			request_description = req_data.description
			request_data = req_data.data

			log.info("【{}】".format(request_description))
			log.info("[{}] {}".format(request_method, request_url))
			if request_headers:    #判断请求头是否为空。
				log.info("[headers] {}".format(request_headers))

			rsp = None
			if "post" == request_method:
				request_data_json = json.dumps(request_data, ensure_ascii = False, cls = DecimalEncoder)
				log.info("[body] {}".format(request_data_json))
				if request_content_type and ("json" in request_content_type):
					rsp = requests.post(request_url, json = json.loads(request_data_json), files = request_files, headers = request_headers)
				else:
					rsp = requests.post(request_url, data= request_data, files= request_files, headers = request_headers)
			elif "get" == request_method:
				rsp = requests.get(request_url)
			else:
				log.error("请求类型错误")
			if "Content-Type" in rsp.headers:  #判断响应头是否包含Content-Type
				log.info("[response-contentType] {}".format(rsp.headers["Content-Type"]))
			log.info("[response] {}".format(rsp.text))

			return rsp.text
		except Exception as e:
			raise Exception("请求异常：{}".format(e))


if __name__ == "__main__":
	req_data = RequestData()

	req_data.url = "http://www.baidu.com"
	req_data.method = RequestMethodEnum.GET.value
	req_data.description = "请求测试"

	HttpUtils.http_request(req_data)