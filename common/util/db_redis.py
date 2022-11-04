#!/usr/bin/python 
# -*- coding: utf-8 -*-
import redis
from common.util.logger import log
from common.util.read_config import ReadConfig


class DBRedis():
	def __init__(self):
		try:
			cf = ReadConfig()

			# 获取数据库配置
			redis_host = cf.get_redis("redis_host")
			redis_port = cf.get_redis("redis_port")

			self.r = redis.Redis(host = redis_host, port = redis_port, decode_responses = True)
		except Exception as e:
			raise Exception("redis连接失败，错误信息: {}".format(e))

	def get_value_by_key(self, key):
		return self.r.get(key)

	def delete_by_key(self, key):
		self.r.delete(key)
		log.info("redis key = {} 删除成功。".format(key))