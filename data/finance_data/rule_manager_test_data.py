#!/usr/bin/python 
# -*- coding: utf-8 -*-


class RuleManagerTestData():
	@classmethod
	def login_rule_manager_online_data(cls, app_code, loginname, password, login_url):
		test_data = {}

		test_data["appCode"] = app_code
		test_data["loginname"] = loginname
		test_data["password"] = password
		test_data["loginUrl"] = login_url

		return test_data


	@classmethod
	def login_proxy_test_data(cls, app_code, loginname, password, login_url):
		test_data = {}

		test_data["appCode"] = app_code
		test_data["loginname"] = loginname
		test_data["password"] = password
		test_data["loginUrl"] = login_url


	@classmethod
	def esign_test_data(cls, params):
		test_data = {}

		test_data["params"] = params
		test_data["captcha"] = "123456"
		test_data["requestNo"] = "11"

		return test_data


