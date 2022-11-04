#!/usr/bin/python 
# -*- coding: utf-8 -*-
from common.service.finance_service.user_service import UserService
from interface.finance.rule_manager_interface import RuleManagerInterface


class BaseRunner():
	# 接口
	rule_manager = RuleManagerInterface()

	# 服务项目
	user_service = UserService()

