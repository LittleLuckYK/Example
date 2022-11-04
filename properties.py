#!/usr/bin/python 
# -*- coding: utf-8 -*-
import os


"""
环境选择
"""

ENV = "ENV_13.ini"

"""
获取项目绝对路径
"""
# os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pro_dir = os.path.dirname(os.path.abspath(__file__))

"""
获取配置路径
"""
config_dir = os.path.join(pro_dir, "config/")
config_path = os.path.join(config_dir, ENV)

"""
获取日志路径
"""
logs_dir = os.path.join(pro_dir, "logs/")


"""
获取文件路径
"""
files_dir = os.path.join(pro_dir, "data/files/")
files_package_dir = os.path.join(files_dir, "package/")
files_identification_id_dir = os.path.join(files_dir, "identification_card/")


"""
获取临时路径
"""
other_dir = os.path.join(pro_dir, "other/")


if __name__ == "__main__":
	print(pro_dir)