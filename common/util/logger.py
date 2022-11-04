#!/usr/bin/python 
# -*- coding: utf-8 -*-

import logging
import time
from properties import *


class Logger():
	def __init__(self):
		#初始化
		self.logger = logging.getLogger()

		#日志文件路径及名称
		log_name = time.strftime("%Y-%m-%d") + ".txt"
		log_path = os.path.join(logs_dir, log_name)

		#设置日志级别
		self.logger.setLevel(logging.INFO)

		#设置日志格式
		self.formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(thread)d] [%(pathname)s:%(lineno)d] - %(message)s")

		#创建FileHandler,用于写入日志文件。
		fh = logging.FileHandler(log_path, "a", encoding = "utf-8")
		fh.setFormatter(self.formatter)
		# fh.setLevel(logging.NOTSET)

		#创建StreamHandler,用于控制台输出。
		ch = logging.StreamHandler()
		ch.setFormatter(self.formatter)
		# ch.setLevel(logging.INFO)

		#添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	def get_logger(self):
		return self.logger

#创建对象
log = Logger().get_logger()

if __name__ == "__main__":
	log.debug("debug information")
	# log.info("information")
	# log.warning("warning information")
	# log.error("错误信息")
	# log.info(type(log))




