#!/usr/bin/python 
# -*- coding: utf-8 -*-
from common.enums.content_type_enum import ContentTypeEnum
from common.enums.request_method_enum import RequestMethodEnum
from common.enums.system_enum import HostEnum
from interface.base_interface import BaseInterface
from common.annotations.annotation import *
from common.util.request_data import *

class RuleManagerInterface(BaseInterface):

	def __init__(self):
		self.host = self.cf.get_host(HostEnum.RULE_MANAGER)

	@ruquest_send(method = RequestMethodEnum.POST, description = "登录", content_type=ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def login_rule_manager_online(self, data):
		path = "login/in"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data


	@ruquest_send(method=RequestMethodEnum.POST, description="代理登录", content_type=ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def login_proxy(self, data):
		path = "rule/system/proxy/login"

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data


	@ruquest_send(method = RequestMethodEnum.POST, description = "签约", content_type = ContentTypeEnum.APPLICATION_JSON_UTF_8)
	def esign(self, app_code, busi_code, type_code, data):
		path = "api/template/esign/{}/{}/{}".format(app_code, busi_code, type_code)

		req_data = RequestData()
		req_data.url = self.host + path
		req_data.data = data

		return req_data




if __name__ == "__main__":
	pass

