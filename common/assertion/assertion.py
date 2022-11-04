#!/usr/bin/python 
# -*- coding: utf-8 -*-
import json

from common.util.logger import log


class Assertion():

	"""
	判断是否为None
	"""
	@classmethod
	def is_not_none(cls, rsp):
		assert rsp, "数据为None"


	@classmethod
	def is_ok(cls, rsp):
		cls.is_not_none(rsp)
		data = json.loads(rsp)
		assert data["code"] == 200

	"""
	基础断言
	"""
	@classmethod
	def is_success(cls, rsp):
		cls.is_not_none(rsp)
		data = json.loads(rsp)
		assert data["success"] and data["executed"], "请求执行失败"

	"""
	获取App登录token
	"""
	@classmethod
	def get_app_login_token(cls, rsp):
		cls.is_success(rsp)
		user_login_token = json.loads(rsp)["accessToken"]
		log.info("user_login_token = {}".format(user_login_token))

		return user_login_token









if __name__ == "__main__":
	Assertion.is_not_none(3)

