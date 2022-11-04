#!/usr/bin/python 
# -*- coding: utf-8 -*-

from common.database.user_info_database import TLogin
from common.enums.system_enum import DataBaseEnum
from common.util.db_mysql import OrmMysql



class UserService():
	def __init__(self):
		self.db = OrmMysql(DataBaseEnum.USER_INFO.value)


	"""
	获取登陆信息
	"""
	def get_login_info(self, user_gid):
		if user_gid:
			try:
				login_info = self.db.session.query(TLogin).filter(TLogin.user_gid == user_gid).one()
				return  login_info
			except Exception as e:
				raise Exception("获取用户信息失败: {}".format(e))








