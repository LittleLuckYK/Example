#!/usr/bin/python 
# -*- coding: utf-8 -*-
import functools

from common.util.http_utils import HttpUtils
from common.util.logger import log

"""
带参数装饰器
"""
def ruquest_send(method = None, path = None, description = None, content_type = None):
	def decorator(fun):
		@functools.wraps(fun)
		def wrapper(*args, **kw):
			req_data = fun(*args, **kw)  #获取请求数据
			if method:
				req_data.method = method.value
			if path:
				req_data.url = req_data.host + path
			if description:
				req_data.description = description
			if content_type:
				req_data.content_type = content_type.value
			return HttpUtils.http_request(req_data)
		return wrapper
	return decorator


"""
不带参数装饰器
"""
def log_aspect(fun):
	@functools.wraps(fun)
	def wrapper(*args, **kw):
		log.info("call {} start".format(fun.__name__) )
		fun(*args, **kw)
		log.info("call {} end".format(fun.__name__))
		return
	return wrapper