#!/usr/bin/python 
# -*- coding: utf-8 -*-
from enum import Enum, unique
from common.util.logger import log


@unique
class HostEnum(Enum):
	USER_INFO = "用户系统"
	RULE_MANAGER = "权限管理系统"


@unique
class SmsTypeEnum(Enum):
	REGISTER = 0  # 自动登陆
	CHANGE_PASSWORD = 1  # 手动登录


@unique
class DataBaseEnum(Enum):
	USER_INFO = "userInfo"



