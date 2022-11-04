#!/usr/bin/python 
# -*- coding: utf-8 -*-

import configparser
from common.enums.system_enum import HostEnum
from common.util.logger import *

class ReadConfig():
	def __init__(self, config_file = None):
		self.cf = configparser.ConfigParser()
		if config_file:
			self.cf.read(config_file)
		else:
			self.cf.read(config_path)

	"""
	获取数据库配置
	"""
	def get_database(self, name):
		try:
			value = self.cf.get("DATABASE", name)
		except Exception as e:
			raise Exception("获取配置文件中的数据库信息（{}）失败: {}".format(name, e))
		return value


	"""
	获取项目请求地址
	"""
	def get_http(self, name):
		try:
			value = self.cf.get("HTTP", name)
		except Exception as e:
			raise Exception("获取配置文件中的项目（{}）请求地址失败: {}".format(name, e))
		return value


	"""
	获取项目请求地址
	"""
	def get_host(self, name):
		host = None

		if name is HostEnum.RULE_MANAGER:
			host = self.get_http("rule_manager")
		elif name is HostEnum.USER_INFO:
			host = self.get_http("user_info")
		else:
			raise Exception("获取项目 {} 请求地址失败".format(name))

		return host


	"""
	获取账号信息
	"""
	def get_account_info(self, name):
		try:
			value = self.cf.get("AUTH", name)
		except Exception as e:
			raise Exception("获取配置文件中的项目（{}）请求地址失败: {}".format(name, e))
		return value

	"""
	获取Redis配置
	"""
	def get_redis(self, name):
		try:
			value = self.cf.get("REDIS", name)
		except Exception as e:
			raise Exception("获取配置文件中Redis数据（{}）失败: {}".format(name, e))
		return value





if __name__ == "__main__":
	ReadConfig().get_host(HostEnum.RULE_MANAGER)




