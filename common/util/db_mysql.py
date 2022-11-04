#!/usr/bin/python 
# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from common.util.read_config import *
import pymysql
import sqlacodegen

"""
ORM查询方式
"""
class OrmMysql():
	def __init__(self, database):

		try:
			cf = ReadConfig()

			# 获取数据库配置
			db_host = cf.get_database("db_host")
			db_username = cf.get_database("db_username")
			db_password = cf.get_database("db_password")
			db_port = int(cf.get_database("db_port"))

			self.link_address = "mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8".format(
				username = db_username, password = db_password, host = db_host, port = db_port, database = database)

			# 初始化数据库链接
			self.engine = create_engine(self.link_address)

			# 创建DBSession类型
			DBSession = sessionmaker(bind=self.engine)

			# 创建Session对象
			self.session = DBSession()

		except Exception as e:
			raise Exception("数据库连接失败，错误信息: {}".format(e))

	"""
	自动生成ORM实体类
	"""
	def auto_create_table_models(self, table_name):

		out_file = os.path.join(other_dir, "models") # 生成文件路径
		link_address = self.link_address.replace("mysqlconnector", "pymysql")

		cmd = "sqlacodegen --tables {table_name} --outfile {out_file} {link_address}".format(
			table_name = table_name, out_file = out_file, link_address = link_address)   # 拼接命令
		log.info(cmd)
		os.system(cmd)
		log.info("表{} ORM实体类已生成".format(table_name))







