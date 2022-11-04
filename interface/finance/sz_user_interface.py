#!/usr/bin/python 
# -*- coding: utf-8 -*-
from common.enums.content_type_enum import ContentTypeEnum
from common.enums.request_method_enum import RequestMethodEnum
from common.enums.system_enum import HostEnum
from interface.base_interface import BaseInterface
from common.util.random_data import *
from common.annotations.annotation import *
from common.util.request_data import *



class SZUserInterface(BaseInterface):

	def __init__(self):
		self.host = self.cf.get_host(HostEnum.USER_INFO)

	@log_aspect
	@ruquest_send(method = RequestMethodEnum.GET, description = "获取图形验证码")
	def get_verification_image(self, req_sn):
		path = "api/beforeLogin/getVerificationImage?reqSn={}".format(req_sn)

		req_data = RequestData()
		req_data.url = self.host + path

		return req_data

	@ruquest_send(method = RequestMethodEnum.POST, description = "获取手机验证码", content_type = ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def get_sms(self, data):
		path = "api/beforeLogin/getSms"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data


	@ruquest_send(method = RequestMethodEnum.POST, description = "APP注册", content_type = ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def register(self, data):
		path = "api/beforeLogin/register"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data

	@ruquest_send(method = RequestMethodEnum.POST, description = "设置登录密码", content_type = ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def set_password(self, data):
		path = "api/beforeLogin/setPassword"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data

	@ruquest_send(method=RequestMethodEnum.POST, description="查询用户GID信息", content_type=ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def get_user_gid(self, data, token):
		path = "api/commonLogin/queryUserGid"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.headers["X-Auth-Token"] = token
		req_data.data = data

		return req_data

	@ruquest_send(method = RequestMethodEnum.POST, description = "登录APP", content_type = ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def login_by_password(self, data):
		path = "api/beforeLogin/loginByPassword"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data

