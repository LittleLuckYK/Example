#!/usr/bin/python 
# -*- coding: utf-8 -*-
import decimal

class SZUserTestData():


	@classmethod
	def login_by_password_test_data(cls, phone, password, sms_type):
		test_data = {}

		test_data["loginName"] = phone
		test_data["passWord"] = password
		test_data["loginType"] = sms_type

		return test_data


