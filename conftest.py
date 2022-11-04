#!/usr/bin/python 
# -*- coding: utf-8 -*-

import sys
import pytest

from app.base.init_driver import init_driver
from common.assertion.assertion import Assertion
from common.enums.system_enum import HostEnum
from common.util.random_data import get_random_data, get_random_str
from common.util.read_config import ReadConfig


# 设置项目路径
from data.finance_data.rule_manager_test_data import RuleManagerTestData
from interface.finance.rule_manager_interface import RuleManagerInterface

sys.path.append(r"D:\Project\Pycharm\Example")

"""
获取配置文件
"""
@pytest.fixture
def config():
	return ReadConfig()


"""
获取登录token
"""
@pytest.fixture
def portal_login_token(config):

	# 获取配置信息
	host = config.get_host(HostEnum.USER_INFO)
	loginname = config.get_account_info("loginname")
	password = config.get_account_info("password")
	app_code = config.get_account_info("app_code")
	url = host + "login/in"

	# 发起登录请求
	rsp = RuleManagerInterface().login_proxy(RuleManagerTestData.login_proxy_test_data(app_code, loginname, password, url))
	portal_login_token = Assertion.get_portal_login_token(rsp)

	return portal_login_token



"""
获取基本信息
"""
@pytest.fixture
def base_data():
	return list(get_random_data())


"""
生成基础数据
"""
@pytest.fixture
def preare_data_sz(base_data, portal_login_token):
	req_sn = get_random_str(6)
	base_data.append(req_sn)
	base_data.append(portal_login_token)

	return  base_data


"""
生成驱动器
"""
@pytest.fixture
def driver():
	return init_driver()




